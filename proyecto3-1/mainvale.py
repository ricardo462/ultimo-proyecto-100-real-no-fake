import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import decimate

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
