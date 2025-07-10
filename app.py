
import streamlit as st
from PIL import Image

st.set_page_config(page_title="BraveFit", layout="wide")

st.markdown("""
<div style='position: absolute; top: 10px; right: 20px; text-align: center; z-index: 100;'>
    <a href='https://www.youtube.com/@Shaurya-h6c' target='_blank' style='text-decoration: none;'>
        <img src='https://raw.githubusercontent.com/ShauryaUpreti1612/bmi-health-adviser/main/logo.jpg' width='80' style='border-radius: 10px;'><br>
        <button style='margin-top: 8px; padding: 6px 12px; font-size: 14px; background-color: #e63946; color: white; border: none; border-radius: 5px; cursor: pointer;'>
            Visit My Channel
        </button>
    </a>
</div>
""", unsafe_allow_html=True)


# Intro text
st.markdown("""
<div style='text-align: left;'>
    <h1 style="font-family: 'Georgia', serif; font-size: 3em; font-weight: bold; letter-spacing: 1px; margin-bottom: 0.2em;">
        BraveFit
    </h1>
    <h4 style="color: gray; font-family: sans-serif; margin-top: 0;">
        Created by Shaurya
    </h4>
</div>

This interactive app helps you understand whether you're in good physical shape.

We classify health into four categories based on BMI:  
<b>Underweight</b>, <b>Normal</b>, <b>Overweight</b>, and <b>Obese</b>.

You’ll be asked to enter your <b>age</b>, <b>gender</b>, <b>weight</b>, and <b>height</b>.<br>
Using this information, we’ll calculate your <b>Body Mass Index (BMI)</b> and give you personalized advice.

➡️ <i>After entering your age, press the <b>Enter</b> key to continue.</i>
""", unsafe_allow_html=True)

# Load images
img_dumbbell = Image.open("dumbbell.png")
img_eating = Image.open("eating.png")

# BMI calculation functions
def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def get_bmi_category(age, gender, bmi):
    if bmi < 15:
        return "Underweight"
    elif 15 <= bmi < 22:
        return "Normal weight"
    elif 22 <= bmi < 25:
        return "Overweight"
    else:
        return "Obese"

# Three‑column layout
left_col, mid_col, right_col = st.columns([1, 2, 1])

with left_col:
    st.image(img_dumbbell, caption="💪 Strength Training", use_container_width=True)
    st.image(img_eating, caption="🥗 Healthy Eating", use_container_width=True)

with mid_col:
    st.title("🏋️‍♂️ BraveFit")
    st.write("Find out your Body Mass Index (BMI) and get personalized advice.")

    age = st.number_input("Enter your age", min_value=1, max_value=120)
    gender = st.selectbox("Select your gender", ["Male", "Female"])
    weight = st.number_input("Enter your weight (in kg)", min_value=1.0, max_value=200.0)
    height = st.number_input("Enter your height (in cm)", min_value=50.0, max_value=250.0)

    if st.button("✅ Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(age, gender.lower(), bmi)

        st.subheader(f"📊 Your BMI: `{bmi:.2f}`")
        st.subheader(f"📌 Category: `{category}`")

        if category == "Underweight":
            st.info("💡 **Advice:** Eat nutritious, high‑calorie foods and consult a doctor.")
        elif category == "Normal weight":
            st.success("🎉 **Advice:** You’re doing great! Stay active and eat healthy.")
        elif category == "Overweight":
            st.warning("⚠️ **Advice:** Be more active and follow a balanced diet.")
        else:
            st.error("🚨 **Advice:** Focus on consistent healthy habits — smart eating, daily movement, and enough rest.")

with right_col:
    img_treadmill = Image.open("treadmill.png")
    img_skipping = Image.open("skipping.png")

    st.image(img_treadmill, caption="🏃‍♂️ Cardio Workout", use_container_width=True)
    st.image(img_skipping, caption="🤸‍♂️ Skipping Rope", use_container_width=True)

# Footer
st.markdown("""<hr style='margin-top:3em'>
<div style='text-align:center;color:gray;font-size:0.9em;'>
    Created with ❤️ by <strong>Shaurya</strong>
</div>""", unsafe_allow_html=True)
