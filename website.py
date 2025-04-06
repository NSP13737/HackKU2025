import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt  <-- Commented out for now

st.set_page_config()

st.title("Police Dashcam Report Summary")

# Sidebar
st.sidebar.title("Summaries")

if st.sidebar.button("03/02/2025 Summary"):
    st.subheader("Summary for 03/02/2025")
    st.write('a')#Nathan function here)

elif st.sidebar.button("03/07/2025 Summary"):
    st.subheader("Summary for 03/07/2025")
    st.write('a')#Nathan function here)

elif st.sidebar.button("03/09/2025 Summary"):
    st.subheader("Summary for 03/09/2025")
    st.write('a')#Nathan function here)

elif st.sidebar.button("03/14/2025 Summary"):
    st.subheader("Summary for 03/14/2025")
    st.write('a')#Nathan function here)




# Main content
st.subheader("Summary")

if st.button("Generate Recording"):
    st.info("Recording generation triggered (placeholder)")
    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])
    if audio_file:
        st.audio(audio_file, format='audio/mp3')
