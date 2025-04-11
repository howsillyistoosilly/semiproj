import numpy as np

def get_current(voltage):
    I0 = 1e-6  # Simulated to be 1 microamp instead of 1 picoamp
    breakdown_voltage = -0.7

    if voltage >= 0:
        return I0 * (np.exp(25 * voltage) - 1)
    elif voltage > breakdown_voltage:
        return -I0
    else:
        return -1e-2  # -10mA at breakdown

