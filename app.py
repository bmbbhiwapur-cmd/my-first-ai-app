import streamlit as st
import requests

# 1. This makes the title of your website
st.title("🧪 My First AI Chemistry Assistant")
st.write("Welcome! Type a chemical name below, and the AI will analyze it.")

# 2. This creates a text box for the user to type in
user_molecule = st.text_input("What molecule do you want to learn about?", "Aspirin")

# 3. This creates a button
if st.button("Ask the AI"):
    
    st.info("Sending message to AnythingLLM...")
    
    # 4. This is the "envelope" we send to your AI. 
    # (Note: For a beginner, we are just printing a success message here to prove the button works!)
    st.success(f"Success! If AnythingLLM was connected, it would now tell you all about {user_molecule}!")
