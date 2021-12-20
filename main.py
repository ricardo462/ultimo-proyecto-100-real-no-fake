import numpy as np 
import matplotlib.pyplot as plt
from Utils import linear_chirp
import soundfile as sf # para escuchar como se escucha

######## 1 #########
# Variables principales
v_peak_to_peak = 3
T = 1 #tiempo total
f_s = int(42e3)

f_0_down = 3e3
f_f_down = 1.6e3

f_0_up = 300
f_f_up = 1.5e3

# Generación de las señales
t_down, chirp_down = linear_chirp(v_peak_to_peak, T, f_0_down, f_f_down, f_s)
t_up, chirp_up = linear_chirp(v_peak_to_peak, T, f_0_up, f_f_up, f_s)

sf.write('chirp_down.wav', chirp_down , f_s)
sf.write('chirp_up.wav', chirp_up , f_s)


# Realización de gráficos
# Dominio temporal
fig, ax = plt.subplots(nrows=1, ncols=1)
ax.plot(t_down, chirp_down)
plt.title('Señal Chirp Down en el dominio temporal')
plt.xlabel('Tiempo(s)')
plt.ylabel('Amplitud')  ## Falta definir una magnitud para la amplitud
plt.show()

fig, ax = plt.subplots(nrows=1, ncols=1)
ax.plot(t_up, chirp_up)
plt.title('Señal Chirp Up en el dominio temporal')
plt.xlabel('Tiempo(s)')
plt.ylabel('Amplitud')  ## Falta definir una magnitud para la amplitud
plt.show()

# Dominio de la frecuencia

chirp_down_fft = np.abs(np.fft.fft(chirp_down))
chirp_up_fft = np.abs(np.fft.fft(chirp_up))

lenght = len(chirp_up_fft)

freq = np.fft.fftfreq(t_up.shape[-1], 1/f_s)

fig, ax = plt.subplots(nrows=1, ncols=1)
ax.plot(freq, chirp_down_fft)
plt.title('Señal Chirp Down en el dominio de la frecuencia')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')  ## Falta definir una magnitud para la amplitud
plt.show()

fig, ax = plt.subplots(nrows=1, ncols=1)
ax.plot(freq, chirp_up_fft)
plt.title('Señal Chirp Up en el dominio de la frecuencia')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')  ## Falta definir una magnitud para la amplitud
plt.show()