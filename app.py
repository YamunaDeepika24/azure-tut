import streamlit as st

# Title
st.title("Basic Streamlit Web App")

# Text
st.write("Hello! This is a simple Streamlit app.")

# Input
name = st.text_input("Enter your name:")

# Button
if st.button("Submit"):
    st.write(f"Welcome, {name}!")

# Slider example
age = st.slider("Select your age:", 1, 100, 25)
st.write("Your age is:", age)
