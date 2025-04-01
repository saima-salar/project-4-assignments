# BMI Calculator
import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="🤒", layout="centered")

st.title("Project 8: Create a Python Streamlit BMI Calculator Web App")
st.markdown("""
# BMI Calculator
This is a simple BMI calculator that takes **weight and height** as input and calculates the BMI.
""")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Enter your weight in kg", min_value=1.0, format="%.2f")

with col2:
    height = st.number_input("Enter your height in cm", min_value=1.0, format="%.2f")

# Ensure both weight and height are provided correctly
if height > 0 and weight > 0:
    bmi = round(weight / ((height / 100) ** 2), 2)  # Round BMI to 2 decimal places
    st.subheader("Your BMI is:")
    st.markdown(f"**{bmi:.2f}**", unsafe_allow_html=True)
    
    # Debugging
    st.write(f"Debug: Calculated BMI = {bmi:.2f}")

    # Corrected condition logic
    if bmi < 18.5:
        st.warning("You are underweight")
    elif bmi >= 18.5 and bmi < 25:
        st.success("You have a normal weight")
    elif bmi >= 25 and bmi < 30:
        st.warning("You are overweight")
    else:
        st.error("You are obese 🚨")
else:
    st.info("Please enter a valid weight and height.")
