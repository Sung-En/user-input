import streamlit as st
from streamlit_local_storage import LocalStorage

# Initialize local storage
local_storage = LocalStorage()

# Try to retrieve the stored user input
stored_input = local_storage.getItem("user_input")
stored_slider_value = local_storage.getItem("slider_value")
stored_checkbox_value = local_storage.getItem("checkbox_value")

# Default values
default_input = "Enter something"
default_slider_value = 50
default_checkbox_value = False

# Use stored values or default values if not found
if stored_input is None:
    stored_input = default_input
if stored_slider_value is None:
    stored_slider_value = default_slider_value
if stored_checkbox_value is None:
    stored_checkbox_value = default_checkbox_value

# Create two columns to align the button and text
col1, col2 = st.columns([1, 2])  # Adjust the width ratio as per your need

# Place buttons and the default text in the same row
with col1:
    load_user_settings = st.button("Load User Settings")
    load_default_settings = st.button("Load Default Settings")

with col2:
    st.write(default_input)  # Display default text next to the Load Default button

# Streamlit widgets for user input
user_input = st.text_input("Enter some text:", value=stored_input)
slider_value = st.slider("Select a number:", 0, 100, value=stored_slider_value)
checkbox_value = st.checkbox("Check this box", value=stored_checkbox_value)

# Display the input values
st.write(f"Current text input: {user_input}")
st.write(f"Current slider value: {slider_value}")
st.write(f"Current checkbox value: {checkbox_value}")

# Save the updated settings to local storage when the "Save Settings" button is pressed
if st.button("Save Settings"):
    local_storage.setItem("user_input", user_input, key="user_input_key")
    local_storage.setItem("slider_value", slider_value, key="slider_key")
    local_storage.setItem("checkbox_value", checkbox_value, key="checkbox_key")

    # Show confirmation
    st.write("Settings saved to local storage")
