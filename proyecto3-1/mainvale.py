import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import decimate, firls

if __name__ == '__main__':
    fase = []
    cuadratura = []
    f = open("muestras/muestras_101_7.bin","rb")
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

    