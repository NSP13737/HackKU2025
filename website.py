import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Police Dashcam Report Summary")
st.write()

num_summary = 0 #Reference later
uploaded_file = st.file_uploader("Choose a JSON file", type="json")

if uploaded_file is not None:
    st.write("File uploaded... ")

    st.subheader("Summary", num_summary)
    if st.button("Generate Recording"):
        st.audio_input()