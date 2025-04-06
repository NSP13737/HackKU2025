import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt  <-- Commented out for now
from AudioTranscriberMultithreaded import AudioTranscriber
import time
import keyboard
from TranscriptPathSummarizer import TranscriptSummarizer



st.set_page_config()

st.title("Police Dashcam Report Summary")


# Sidebar
st.sidebar.title("Summaries")

if st.sidebar.button("Summarize file path"):
    summarizer = TranscriptSummarizer()
    summary = summarizer.generate_summary()
    st.write(summary)

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

if st.button("Start Recording"):
    transcriber = AudioTranscriber(officer_number="002")
    st.info("Recording generation triggered. Press the Spacebar to stop. You can view the output in the terminal")
    transcriber.start_processing()
    keyboard.wait('space')
    print("Recording stopped.")
    transcriber.stop_processing()
    summarizer = TranscriptSummarizer(officer_number="002")
    summary2 = summarizer.generate_summary()
    print(summary2)
    st.write(summary2)


    
