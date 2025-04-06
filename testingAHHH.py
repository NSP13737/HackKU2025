from AudioTranscriber import AudioTranscriber
import keyboard

# Initialize the AudioTranscriber
transcriber = AudioTranscriber()

print("Press 'p' to start recording and 'q' to stop recording.")

# Wait for the 'p' key to start processing
keyboard.wait('p')
print("Recording started.")
transcriber.start_processing()

# Wait for the 'q' key to stop processing
keyboard.wait('q')
print("Recording stopped.")
transcriber.stop_processing()

print("Processing complete. Transcript saved at:", transcriber.transcript)