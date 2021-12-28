from Utils import plot_fft
import numpy as np
if __name__ == '__main__':
    name_signals = ['muestras_101_7', 'muestras_TV']
    signals = []
    samples_per_second = 1e6
    signal_length = 10 # seconds
    time_step = 1 / samples_per_second / signal_length
    
    for name_signal in name_signals:
        f = open('muestras/' + name_signal + '.bin',"rb")
        data = np.fromfile(f, 'int8')

        signal, fase, cuadratura = [], [], []

        for i, value in enumerate(data):
            if i%2 == 0:
                fase.append(value)
            else:
                cuadratura.append(value)

        for i in range(len(fase)):
            signal.append(fase[i] + 1j* cuadratura[i])

        plot_fft(signal, time_step, name_signal)
