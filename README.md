# 🔬 PN Junction Virtual Lab (Streamlit)

An interactive virtual electronics lab built using Python and Streamlit to simulate the **PN junction diode I-V characteristics**. Great for students learning semiconductor basics.

---

## 🧪 Features

- Choose **Forward or Reverse Bias**
- Apply voltages from **-5V to +5V**
- Measure diode current behavior (exponential in forward, saturation in reverse)
- Plot and visualize the **I-V curve**
- Reset the experiment anytime
- Supports up to **10 voltage/current readings**
- **Linear interpolation** used to avoid noisy spline artifacts

---

## 🚀 Live Demo

Run locally with Streamlit:

```bash
pip install streamlit matplotlib numpy scipy
streamlit run app.py
