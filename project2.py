import streamlit as st
import random

st.title("📘 Class 12 Physics Chapter Quiz Generator")
st.write("Select a chapter and answer 3 random MCQs. Score will be shown after submitting all answers.")

# Full 14 chapters with multiple questions
quiz_bank = {
    "Electrostatics": [
        ("SI unit of electric charge is?", ["Coulomb", "Ampere", "Volt", "Ohm"], "Coulomb"),
        ("Electric field is defined as force per unit?", ["Charge", "Mass", "Time", "Current"], "Charge"),
        ("Which law gives force between two charges?", ["Coulomb’s law", "Ohm’s law", "Faraday’s law", "Gauss law"], "Coulomb’s law"),
        ("Electric potential is a ___ quantity.", ["Scalar", "Vector", "Tensor", "None"], "Scalar")
    ],
    "Current Electricity": [
        ("SI unit of electric current is?", ["Ampere", "Volt", "Ohm", "Watt"], "Ampere"),
        ("Ohm’s law is V ∝ ?", ["I", "R", "1/R", "I²"], "I"),
        ("Resistance depends on?", ["Length", "Area", "Material", "All of these"], "All of these"),
        ("Unit of resistivity is?", ["Ohm-m", "Ohm", "m/Ohm", "Ohm/m"], "Ohm-m")
    ],
    "Magnetic Effects of Current": [
        ("SI unit of magnetic field is?", ["Tesla", "Weber", "Henry", "Gauss"], "Tesla"),
        ("Who discovered electromagnetic induction?", ["Faraday", "Newton", "Maxwell", "Ampere"], "Faraday"),
        ("Magnetic field around a straight conductor is?", ["Circular", "Linear", "Elliptical", "Random"], "Circular"),
        ("Right hand thumb rule is used to find?", ["Direction of magnetic field", "Current", "Force", "Voltage"], "Direction of magnetic field")
    ],
    "Electromagnetic Induction": [
        ("Induced emf depends on rate of change of?", ["Magnetic flux", "Current", "Charge", "Resistance"], "Magnetic flux"),
        ("Lenz’s law is based on law of?", ["Conservation of energy", "Motion", "Charge", "Mass"], "Conservation of energy"),
        ("SI unit of magnetic flux is?", ["Weber", "Tesla", "Henry", "Ampere"], "Weber"),
        ("Eddy currents produce?", ["Heat", "Light", "Sound", "Radiation"], "Heat")
    ],
    "Alternating Current": [
        ("Average value of AC over a full cycle is?", ["Zero", "Maximum", "Minimum", "Infinity"], "Zero"),
        ("RMS value of AC is related to?", ["Heating effect", "Magnetic effect", "Chemical effect", "Radiation"], "Heating effect"),
        ("Frequency of AC in India is?", ["50 Hz", "60 Hz", "100 Hz", "25 Hz"], "50 Hz"),
        ("Pure inductor circuit current ___ voltage.", ["Lags", "Leads", "Equals", "Opposes"], "Lags")
    ],
    "Electromagnetic Waves": [
        ("Which wave has the highest frequency?", ["Radio waves", "Microwaves", "X-rays", "Infrared"], "X-rays"),
        ("Electromagnetic waves travel at?", ["Speed of light", "Sound speed", "Electron speed", "Zero"], "Speed of light"),
        ("EM waves are ___ waves.", ["Transverse", "Longitudinal", "Surface", "None"], "Transverse")
    ],
    "Ray Optics": [
        ("Mirror formula is 1/f = ?", ["1/v + 1/u", "v/u", "u/v", "f/v"], "1/v + 1/u"),
        ("Power of lens is measured in?", ["Dioptre", "Watt", "Tesla", "Volt"], "Dioptre"),
        ("Convex lens is also called?", ["Converging lens", "Diverging lens", "Plane lens", "Cylindrical lens"], "Converging lens"),
        ("Refractive index is ratio of?", ["Speeds", "Wavelengths", "Frequencies", "Angles"], "Speeds")
    ],
    "Wave Optics": [
        ("Interference is based on principle of?", ["Superposition", "Reflection", "Refraction", "Diffraction"], "Superposition"),
        ("Young’s double slit experiment proves nature of light as?", ["Wave", "Particle", "Both", "None"], "Wave"),
        ("Fringe width depends on?", ["Wavelength", "Distance", "Slit separation", "All of these"], "All of these"),
        ("Diffraction is prominent when?", ["Aperture ~ wavelength", "Large aperture", "Small wavelength", "None"], "Aperture ~ wavelength")
    ],
    "Dual Nature of Radiation and Matter": [
        ("Photoelectric effect supports nature of light as?", ["Particle", "Wave", "Both", "None"], "Particle"),
        ("Photon has?", ["Zero mass", "Negative mass", "Positive mass", "Variable mass"], "Zero mass"),
        ("Energy of photon is proportional to?", ["Frequency", "Wavelength", "Speed", "Amplitude"], "Frequency"),
        ("Threshold frequency depends on?", ["Material", "Intensity", "Distance", "Time"], "Material")
    ],
    "Atoms": [
        ("Rutherford model failed to explain?", ["Stability of atom", "Charge", "Mass", "Volume"], "Stability of atom"),
        ("Bohr model applies to?", ["Hydrogen atom", "All atoms", "Molecules", "Ions"], "Hydrogen atom"),
        ("Angular momentum of electron is?", ["Quantized", "Continuous", "Zero", "Infinite"], "Quantized"),
        ("Atomic spectra are?", ["Line spectra", "Continuous", "Band", "Random"], "Line spectra")
    ],
    "Nuclei": [
        ("SI unit of radioactive activity is?", ["Becquerel", "Curie", "Gray", "Sievert"], "Becquerel"),
        ("Binding energy is due to?", ["Mass defect", "Charge", "Volume", "Density"], "Mass defect"),
        ("Most stable nucleus has mass number?", ["Around 56", "10", "100", "200"], "Around 56"),
        ("Nuclear force is?", ["Short range", "Long range", "Gravitational", "Electromagnetic"], "Short range")
    ],
    "Semiconductor Electronics": [
        ("Pure semiconductor is called?", ["Intrinsic", "Extrinsic", "Conductor", "Insulator"], "Intrinsic"),
        ("Most commonly used semiconductor is?", ["Silicon", "Copper", "Iron", "Silver"], "Silicon"),
        ("PN junction diode allows current in?", ["One direction", "Both directions", "None", "Reverse only"], "One direction"),
        ("Logic gate OR gives output 1 when?", ["Any input is 1", "All inputs are 1", "All inputs are 0", "None"], "Any input is 1")
    ],
    "Communication Systems": [
        ("Communication system consists of?", ["Transmitter, channel, receiver", "Only transmitter", "Only receiver", "Antenna"], "Transmitter, channel, receiver"),
        ("Modulation is used to?", ["Reduce antenna height", "Increase noise", "Decrease range", "Remove signal"], "Reduce antenna height"),
        ("Bandwidth is difference between?", ["Highest and lowest frequency", "Amplitude", "Speed", "Time"], "Highest and lowest frequency"),
        ("AM stands for?", ["Amplitude Modulation", "Angle Modulation", "Analog Modulation", "Automatic Modulation"], "Amplitude Modulation")
    ]
}

# Initialize score in session state
if "score" not in st.session_state:
    st.session_state.score = 0

# Chapter selection
chapter = st.selectbox("Select a Class 12 Physics Chapter", list(quiz_bank.keys()))

# Randomly pick 3 questions
questions = random.sample(quiz_bank[chapter], 3)

# Initialize answers in session_state
for i in range(3):
    key = f"{chapter}_{i}"
    if key not in st.session_state:
        st.session_state[key] = None

st.subheader(f"Quiz on: {chapter}")

# Display questions safely
for i, (q_text, options, ans) in enumerate(questions):
    key = f"{chapter}_{i}"
    selection = st.radio(f"Q{i+1}. {q_text}", options, key=key)
    st.session_state[key] = selection

# Submit button
if st.button("Submit Quiz"):
    st.session_state.score = 0
    for i, (_, _, ans) in enumerate(questions):
        key = f"{chapter}_{i}"
        selected = st.session_state[key]
        if selected == ans:
            st.session_state.score += 1
    st.success(f"Your Score for {chapter}: {st.session_state.score} / 3")
