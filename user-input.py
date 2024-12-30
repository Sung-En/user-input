import streamlit as st
from streamlit_local_storage import LocalStorage

# Initialize local storage
local_storage = LocalStorage()

# Title of the app
st.title("Persistent User Input Example")

# Try to retrieve previous input from localStorage, if any
stored_input = local_storage.getItem("user_input")
stored_slider_value = local_storage.getItem("slider_value")
stored_checkbox_value = local_storage.getItem("checkbox_value")

# Initialize default values if no stored values are found
default_input = ""
default_slider_value = 50
default_checkbox_value = False

# Use stored values or fall back to defaults only once when the app first loads
if stored_input is None:
    stored_input = default_input
if stored_slider_value is None:
    stored_slider_value = default_slider_value
if stored_checkbox_value is None:
    stored_checkbox_value = default_checkbox_value

# Now, let the user interact with the widgets
user_input = st.text_input("Enter some text:", value=stored_input, key="user_input_unique_key")
slider_value = st.slider("Select a number:", 0, 100, value=stored_slider_value, key="slider_unique_key")
checkbox_value = st.checkbox("Check this box", value=stored_checkbox_value, key="checkbox_unique_key")

# Debug: Show the current input values
st.write(f"Current input (text): {user_input}")
st.write(f"Current slider value: {slider_value}")
st.write(f"Current checkbox value: {checkbox_value}")

# Button to save settings to local storage
if st.button("Save Settings"):
    # Save input values to localStorage
    local_storage.setItem("user_input", user_input)
    local_storage.setItem("slider_value", slider_value)
    local_storage.setItem("checkbox_value", checkbox_value)

    # Debug: Confirm that values have been saved to local storage
    st.write("Values saved to local storage:")
    st.write(f"Saved user input: {user_input}")
    st.write(f"Saved slider value: {slider_value}")
    st.write(f"Saved checkbox value: {checkbox_value}")

# Display retained values
st.write(f"Text input: {user_input}")
st.write(f"Slider value: {slider_value}")
st.write(f"Checkbox value: {checkbox_value}")
