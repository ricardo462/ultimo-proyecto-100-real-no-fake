import numpy as np

def linear_chirp(peak_to_peak, T, initial_frecuency, final_frecuency, f_s = 48e3, initial_phase=0):
    c = (final_frecuency - initial_frecuency) / T
    t = np.linspace(0, T, f_s*T)
    x = peak_to_peak/2 * np.sin(initial_phase + 2*np.pi*(c*t**2/2 + initial_frecuency * t))
    return t,x
