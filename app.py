
import streamlit as st
from PIL import Image

st.set_page_config(page_title="BraveFit", layout="centered")

# YouTube + Logo (centered for mobile-first)
st.markdown("""
<div style='text-align: center; margin-top: 10px;'>
    <a href='https://www.youtube.com/@Shaurya-h6c' target='_blank' style='text-decoration: none;'>
        <img src='https://raw.githubusercontent.com/ShauryaUpreti1612/bmi-health-adviser/main/logo.jpg' style='width: 30vw; max-width: 120px; border-radius: 10px;'><br>
        <div style='margin-top: 8px; display: inline-block; padding: 6px 14px; font-size: 14px; font-weight: bold; background-color: #e63946; color: white; border-radius: 5px;'>
            Visit My Channel
        </div>
    </a>
</div>
""", unsafe_allow_html=True)

# Intro text
st.markdown("""
<div style='text-align: center;'>
    <h1 style="font-family: 'Georgia', serif; font-size: 2.5em; font-weight: bold; letter-spacing: 1px; margin-bottom: 0.2em;">
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
img_treadmill = Image.open("treadmill.png")
img_skipping = Image.open("skipping.png")

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

# Display images responsively
st.image([img_dumbbell, img_eating], caption=["💪 Strength Training", "🥗 Healthy Eating"], width=180)
st.image([img_treadmill, img_skipping], caption=["🏃‍♂️ Cardio Workout", "🤸‍♂️ Skipping Rope"], width=180)

st.markdown("### 🧮 Calculate Your BMI")
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

# Footer
st.markdown("""<hr style='margin-top:3em'>
<div style='text-align:center;color:gray;font-size:0.9em;'>
    Created with ❤️ by <strong>Shaurya</strong>
</div>""", unsafe_allow_html=True)
