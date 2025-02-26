import streamlit as st
import random

# Generate a random number
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 10)

# Custom CSS for Styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f5f7fa; /* Light Background */
            padding: 20px;
            text-align: center;
        }

        /* Input box design */
        div[data-baseweb="input"] {
            background-color: #ffcc00; /* Yellow Input Box */
            color: black;
            font-weight: bold;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
            border-radius: 8px;
            padding: 10px;
        }

        /* Button design */
        button {
            background-color: #ff4500 !important; /* Bright Orange Button */
            color: white !important;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
        }

        /* Title Styling */
        h1 {
            color: #333;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.3);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🎲 Guess the Secret Number!")

# Instructions
st.write("🧠 **Computer ne 1️⃣ - 🔟 tak ek secret number socha hai.**") 
st.write("🎯 **Aapko us number ko guess karna hai.**")
st.write("💡 **Hint milega agar guess zyada ya kam hoga!**")

# User Input
user_guess = st.number_input("🔢 **Enter your lucky guess:**", min_value=1, max_value=10, step=1)

# Check Button
if st.button("🎰 Try My Luck!"):
    if user_guess == st.session_state.random_number:
        st.success(f"🏆 **Wah! Bilkul sahi!** Number tha **{st.session_state.random_number}**! 🎊🎉")

        # Show Balloons Animation on Win
        st.balloons()

        # Generate a new number for the next round
        st.session_state.random_number = random.randint(1, 10)  
    elif user_guess < st.session_state.random_number:
        st.warning("📉 **Too low!** Thoda aur bara try karo. 📈")
    else:
        st.warning("📈 **Too high!** Thoda aur chhota socho. 📉")
