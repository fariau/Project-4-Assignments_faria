import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    character_pool = string.ascii_letters
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        return "Select at least one character type"

    return ''.join(random.choice(character_pool) for _ in range(length))

st.title("🔑 Password Generator")

# User input
length = st.slider("Select password length", min_value=4, max_value=30, value=12)
use_digits = st.checkbox("Include digits")
use_special = st.checkbox("Include special characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success("Generated Password:")
    st.code(password, language="text")
    
    # Copy button
    st.button("Copy to Clipboard", on_click=lambda: st.write("Use Ctrl+C or Cmd+C to copy!"))

st.write("---------")
st.markdown("🚀 Built by [Faria Usman](#) – Stay secure, stay strong! 🔐")


