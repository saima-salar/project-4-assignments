# Project-8-python-streamlit-bmi-calculator

GIAIC

https://saimasalarproject-8-python-app-bmi-calculator.streamlit.app/

This Streamlit-based BMI Calculator allows users to input their weight (kg) and height (cm) to compute their Body Mass Index (BMI) and categorize it accordingly.


🔹 Key Features:


Streamlit UI Setup


Uses st.set_page_config() to set page title and icon.


Displays a title and description using st.title() and st.markdown().


User Input Fields


Uses two columns (st.columns(2)) for a structured UI.


st.number_input() takes weight (kg) and height (cm) with a minimum value of 1.0.


BMI Calculation


Formula:

𝐵
𝑀
𝐼
=
weight (kg)
(
height (m)
)
2
BMI= 
(height (m)) 
2
 
weight (kg)
​
 
Height is converted from cm to meters (height / 100).


BMI is rounded to 2 decimal places.


BMI Classification Logic


Underweight: BMI < 18.5


Normal Weight: 18.5 ≤ BMI < 25


Overweight: 25 ≤ BMI < 30


Obese: BMI ≥ 30


Uses st.warning(), st.success(), and st.error() to display appropriate messages.


Error Handling & Debugging


Ensures both height and weight are valid before calculation.


Prints debugging information (st.write(f"Debug: Calculated BMI = {bmi:.2f}")).


Displays an info message (st.info()) if values are invalid.


🛠️ Possible Improvements:


✅ Remove debugging output (st.write(f"Debug: Calculated BMI = {bmi:.2f}")) for a cleaner UI.


✅ Add a BMI interpretation guide or color-coded results for better UX.


✅ Use st.image() to visually represent BMI categories.













