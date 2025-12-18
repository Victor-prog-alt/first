import streamlit as st
st.title("my first project")
name = st.text_input("whats your name")
if name:
  st.write(f"Hello, {name}!")
