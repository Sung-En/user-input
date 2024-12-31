import streamlit as st
from streamlit_local_storage import LocalStorage

# Initialize local storage
local_storage = LocalStorage()

# Default values
default_input = "Enter something"
default_slider_value = 50
default_checkbox_value = False

# Try to retrieve the stored user input, slider, and checkbox values
stored_input = local_storage.getItem("user_input")
stored_slider_value = local_storage.getItem("slider_value")
stored_checkbox_value = local_storage.getItem("checkbox_value")

# Use stored values or default values if not found
if stored_input is None:
    stored_input = default_input
if stored_slider_value is None:
    stored_slider_value = default_slider_value
if stored_checkbox_value is None:
    stored_checkbox_value = default_checkbox_value

# Initialize session state to retain the settings across reruns
if "user_input" not in st.session_state:
    st.session_state.user_input = stored_input
if "slider_value" not in st.session_state:
    st.session_state.slider_value = stored_slider_value
if "checkbox_value" not in st.session_state:
    st.session_state.checkbox_value = stored_checkbox_value

# Add buttons to load settings
if st.button("Load User Settings"):
    # Load the saved user settings into session state
    st.session_state.user_input = stored_input
    st.session_state.slider_value = stored_slider_value
    st.session_state.checkbox_value = stored_checkbox_value

if st.button("Load Default Settings"):
    # Load the default settings into session state
    st.session_state.user_input = default_input
    st.session_state.slider_value = default_slider_value
    st.session_state.checkbox_value = default_checkbox_value

# Display the text to show which settings are loaded
st.write(f"User saved text: {st.session_state.user_input}")
st.write(f"Default text: {default_input}")

# Streamlit widgets for user input
user_input = st.text_input("Enter some text:", value=st.session_state.user_input)
slider_value = st.slider("Select a number:", 0, 100, value=st.session_state.slider_value)
checkbox_value = st.checkbox("Check this box", value=st.session_state.checkbox_value)

# Display the current values
st.write(f"Current text input: {user_input}")
st.write(f"Current slider value: {slider_value}")
st.write(f"Current checkbox value: {checkbox_value}")

# Save the updated settings to local storage when "Save Settings" is clicked
if st.button("Save Settings"):
    # Save user input, slider value, and checkbox value to local storage
    local_storage.setItem("user_input", user_input, key="user_input_key")
    local_storage.setItem("slider_value", slider_value, key="slider_key")
    local_storage.setItem("checkbox_value", checkbox_value, key="checkbox_key")

    # Update session state with the new values
    st.session_state.user_input = user_input
    st.session_state.slider_value = slider_value
    st.session_state.checkbox_value = checkbox_value

    # Show confirmation
    st.write("Settings saved to local storage")
