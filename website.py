import streamlit as st
from AudioTranscriber import AudioTranscriber

#Example below
transcriber = AudioTranscriber()
transcriber.start_processing()
transcriber.stop_processing()
st.write(f"Transcript saved at: {transcriber.transcript}")
