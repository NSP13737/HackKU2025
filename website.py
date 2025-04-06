import streamlit as st
import pandas as pd
<<<<<<< HEAD
=======
# import matplotlib.pyplot as plt  <-- Commented out for now
from AudioTranscriberMultithreaded import AudioTranscriber
import time
import keyboard
from TranscriptPathSummarizer import TranscriptSummarizer

#Example below
transcriber = AudioTranscriber()
>>>>>>> 3406cd703138b585f1f05b760db09f28612efd69

st.set_page_config(page_title="OWL - Observational Watch Log")

st.title("OWL - Observational Watch Log")

<<<<<<< HEAD
#Produce an image
# Load image
from PIL import Image
owl_image = Image.open("A_flat_vector_illustration_features_a_stylized_owl.png")

# Display the image in top right using HTML and base64 encoding
import base64
from io import BytesIO

# Convert image to base64
buffered = BytesIO()
owl_image.save(buffered, format="PNG")
img_b64 = base64.b64encode(buffered.getvalue()).decode()

# HTML for top-right positioning
st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 30px;">
        <h1 style="margin: 0;">OWL - Observational Watch Log</h1>
        <img src="data:image/png;base64,{img_b64}" width="100" style="margin-top: 5px;" />
    </div>
""", unsafe_allow_html=True)

# Initialize session state for the selected summary
if "selected_summary" not in st.session_state:
    st.session_state.selected_summary = None

# Sidebar: Summary buttons
=======

# Sidebar
>>>>>>> 3406cd703138b585f1f05b760db09f28612efd69
st.sidebar.title("Summaries")

if st.sidebar.button("Summarize file path"):
    summarizer = TranscriptSummarizer()
    summary = summarizer.generate_summary()
    st.write(summary)

if st.sidebar.button("03/02/2025 Summary"):
    st.session_state.selected_summary = "03/02/2025"
if st.sidebar.button("03/07/2025 Summary"):
    st.session_state.selected_summary = "03/07/2025"
if st.sidebar.button("03/09/2025 Summary"):
    st.session_state.selected_summary = "03/09/2025"
if st.sidebar.button("03/14/2025 Summary"):
    st.session_state.selected_summary = "03/14/2025"

# Main content area
if st.session_state.selected_summary:
    # Display the selected summary
    st.subheader(f"Summary for {st.session_state.selected_summary}")
    st.write("a")  # Replace with your function call or summary text

    # Back button to reset view
    if st.button("Back"):
        st.session_state.selected_summary = None
else:
    # Default main page view
    st.subheader("Summary")
    if st.button("Generate Recording"):
        st.info("Recording generation triggered (placeholder)")
        audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])
        if audio_file:
            st.audio(audio_file, format='audio/mp3')


<<<<<<< HEAD
=======




# Main content
st.subheader("Summary")

if st.button("Start Recording"):
    st.info("Recording generation triggered. Press the Spacebar to stop.")
    transcriber.start_processing()
    keyboard.wait('space')
    print("Recording stopped.")
    transcriber.stop_processing()
    # audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])
    # if audio_file:
    #     st.audio(audio_file, format='audio/mp3')


    
>>>>>>> 3406cd703138b585f1f05b760db09f28612efd69
