import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

st.set_page_config(page_title="PN Junction Virtual Lab", layout="centered")

st.title("🔬 PN Junction Characteristics Simulator")

# Simulate diode behavior
def get_current(voltage):
    I0 = 1e-6  # 1 µA reverse saturation current
    breakdown_voltage = -0.7  # Reverse breakdown voltage

    if voltage >= 0:
        return I0 * (np.exp(25 * voltage) - 1)
    elif voltage > breakdown_voltage:
        return -I0
    else:
        return -1e-2  # Simulate breakdown current

# App session state
if "readings" not in st.session_state:
    st.session_state.readings = []

# Input area
with st.form("input_form"):
    bias_type = st.radio("Select Bias Type:", ["Forward", "Reverse"], horizontal=True)
    voltage = st.slider("Set Voltage (V):", -5.0, 5.0, 0.0, 0.1)
    submitted = st.form_submit_button("Measure Current")

    if submitted:
        if len(st.session_state.readings) >= 10:
            st.warning("You can only take 10 readings.")
        else:
            v = abs(voltage) if bias_type == "Forward" else -abs(voltage)
            current = get_current(v)
            st.session_state.readings.append((v, current))
            st.success(f"Measured Current: {current:.3e} A at {v:.2f} V")

# Display current table
if st.session_state.readings:
    st.subheader("Measured Values")
    st.table({
        "Voltage (V)": [f"{v:.2f}" for v, _ in st.session_state.readings],
        "Current (A)": [f"{i:.3e}" for _, i in st.session_state.readings]
    })

# Plot graph
if st.button("Plot I-V Graph") and st.session_state.readings:
    st.subheader("PN Junction I-V Characteristics")

    # Remove duplicate voltages
    unique = {}
    for v, i in st.session_state.readings:
        unique[v] = i
    voltages = np.array(sorted(unique.keys()))
    currents = np.array([unique[v] for v in voltages])

    fig, ax = plt.subplots()
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    # Linear interpolation
    if len(voltages) >= 2:
        x_smooth = np.linspace(voltages.min(), voltages.max(), 200)
        linear_interp = interp1d(voltages, currents, kind='linear')
        y_smooth = linear_interp(x_smooth)
        ax.plot(x_smooth, y_smooth, color='blue', label='I-V Curve')

    # Plot actual points
    ax.plot(voltages, currents, 'ro', label='Data Points')
    ax.set_xlabel("Voltage (V)")
    ax.set_ylabel("Current (A)")
    ax.set_title("PN Junction I-V Characteristics")
    ax.grid(True)
    ax.legend()
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-0.02, 0.05)

    st.pyplot(fig)

# Reset
if st.button("Reset Experiment"):
    st.session_state.readings = []
