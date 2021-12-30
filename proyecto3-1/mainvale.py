import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import decimate, firls
import soundfile as sf

if __name__ == '__main__':
    muestras = ['muestras_88_9.bin', 'muestras_94_1.bin', 'muestras_101_7.bin', 'muestras_104_9.bin', 'muestras_TV.bin']

    for muestra in muestras: 
        fase = []
        cuadratura = []
        f = open("muestras/"+muestra,"rb")
        data = np.fromfile(f, 'int8')

        signal, fase, cuadratura = [], [], []

        for i, value in enumerate(data):
            if i%2 == 0:
                fase.append(value)
            else:
                cuadratura.append(value)

        for i in range(len(fase)):
            signal.append(fase[i] + 1j* cuadratura[i])

        espectro = fft(signal)
        espec = espectro/max(espectro)

        dec_espectro = 20*np.log10(espec)

        fir_df = decimate(signal, 8, ftype='fir')

        dif = firls(29, [0, 0.9], [0, 1.0])

        fir_df_norm = fir_df/abs(fir_df)

        fir_real = fir_df_norm.real
        fir_imag = fir_df_norm.imag

        y_FM_dem = (fir_real * np.convolve(fir_imag, dif, 'same') - fir_imag*np.convolve(fir_real,dif,'same'))/(fir_real**2 + fir_imag**2)

        df = decimate(y_FM_dem,10,ftype='fir')

        freqs = [10.5e3, 11e3, 12e3, 13e3]
        for freq in freqs:
            sf.write("audios/"+muestra+str(freq)+'.wav', df , int(freq))
