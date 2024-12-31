import streamlit as st
from streamlit_local_storage import LocalStorage

# Initialize local storage
local_storage = LocalStorage()

# Default settings
default_settings = {
    "slider_value": 50,
    "text_input": "Default Text",
}

# Retrieve previous values from local storage, if available
stored_slider_value = local_storage.getItem("slider_value")  # itemKey
stored_text_input = local_storage.getItem("text_input")  # itemKey

# Use stored settings or default values
slider_value = stored_slider_value if stored_slider_value is not None else default_settings["slider_value"]
text_input_value = stored_text_input if stored_text_input is not None else default_settings["text_input"]

# Streamlit widgets with unique keys to avoid conflicts
slider = st.slider("Slider", 0, 100, value=slider_value, key="slider_key")
text_input = st.text_input("Text Input", value=text_input_value, key="text_input_key")


# Save user settings to local storage
def save_user_settings():
    local_storage.setItem("slider_value", slider, key="slider_key")
    local_storage.setItem("text_input", text_input, key="text_input_key")
    st.write("User settings saved!")


# Buttons and text to display the settings
load_message = st.empty()  # Empty placeholder for the message

# Top Section: Load User Settings button
col1, col2 = st.columns([1, 3])

with col1:
    if st.button("Load User Settings"):
        # Load user settings from local storage
        stored_slider_value = local_storage.getItem("slider_value")
        stored_text_input = local_storage.getItem("text_input")

        # If values are found, update them; otherwise, fallback to defaults
        if stored_slider_value is not None and stored_text_input is not None:
            slider_value = stored_slider_value
            text_input_value = stored_text_input
            load_message.text(f"User settings loaded: Slider Value = {slider_value}, Text Input = {text_input_value}")
        else:
            load_message.text("No user settings found, loading defaults.")

        # Update the slider and text input with the loaded values
        slider = st.slider("Slider", 0, 100, value=slider_value, key="slider_key")
        text_input = st.text_input("Text Input", value=text_input_value, key="text_input_key")

with col2:
    st.write("Text: User settings loaded or defaults if none")

# Top Section: Load Default Settings button
col1, col2 = st.columns([1, 3])

with col1:
    if st.button("Load Default Settings"):
        # Load default settings
        slider_value = default_settings["slider_value"]
        text_input_value = default_settings["text_input"]
        load_message.text(f"Default settings loaded: Slider Value = {slider_value}, Text Input = {text_input_value}")

        # Update the slider and text input with the default values
        slider = st.slider("Slider", 0, 100, value=slider_value, key="slider_key")
        text_input = st.text_input("Text Input", value=text_input_value, key="text_input_key")

with col2:
    st.write("Text: Default settings loaded")

# Bottom Section: Save Settings button
if st.button("Save Settings"):
    save_user_settings()
