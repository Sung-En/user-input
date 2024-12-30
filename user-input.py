import streamlit as st

# Title of the app
st.title("User Input Retention Example")

# Text input for the user
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""  # Initialize if not present

user_input = st.text_input("Enter some text:", st.session_state.user_input)
st.session_state.user_input = user_input  # Retain user input after refresh

# Slider for selecting a value
if 'slider_value' not in st.session_state:
    st.session_state.slider_value = 50  # Initialize slider value if not present

slider_value = st.slider("Select a number:", 0, 100, st.session_state.slider_value)
st.session_state.slider_value = slider_value  # Retain slider value after refresh

# Checkbox to toggle a condition
if 'checkbox_value' not in st.session_state:
    st.session_state.checkbox_value = False  # Initialize checkbox value if not present

checkbox_value = st.checkbox("Check this box", value=st.session_state.checkbox_value)
st.session_state.checkbox_value = checkbox_value  # Retain checkbox state after refresh

# Display retained values
st.write(f"Text input: {st.session_state.user_input}")
st.write(f"Slider value: {st.session_state.slider_value}")
st.write(f"Checkbox value: {st.session_state.checkbox_value}")
