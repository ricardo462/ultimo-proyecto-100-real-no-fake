import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

def plot_fft(signal:np.array, time_step: float, signal_name: str) -> None:
    espectro = np.abs(fft(signal))
    espec = espectro/max(espectro)
    dec_espectro = 20*np.log10(espec)

    n = espectro.size
    frec = fftfreq(n, d=time_step)

    plt.plot(frec, dec_espectro)
    plt.title(f'Espectro de muestras de la señal {signal_name}')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud (dB)')
    plt.savefig(f'figs/fft_{signal_name}')
    plt.show()
