import os
import json
import datetime
import wave
import pyaudio
import whisperx
import time
import keyboard

class AudioTranscriber:
    def __init__(self, officer_number="001", base_path=None, huggingface_token="hf_PHuIpkHZVUjJTAg____iiNZgZhYBHppjvbCWCd"):
        """
        Initializes the AudioTranscriber with necessary paths and configurations.
        """
        # Stuff for threading
        #self.running = False
        #self.loop_thread = None
        #self.transcript = None  # Will hold the transcript path after processing

        self.base_path = base_path or os.getcwd()
        self.officer_number = officer_number
        self.huggingface_token = huggingface_token

        # Define paths based on the officer number
        self.officer_path = os.path.join(self.base_path, f"officer_data/officer_{self.officer_number}")
        self.audio_directory = os.path.join(self.officer_path, 'audio')
        self.transcript_directory = os.path.join(self.officer_path, 'transcripts')

        # Ensure directories exist
        os.makedirs(self.audio_directory, exist_ok=True)
        os.makedirs(self.transcript_directory, exist_ok=True)

        # Initialize PyAudio
        self.p = pyaudio.PyAudio()

    def __del__(self):
        """
        Ensures that the PyAudio instance is terminated.
        """
        if hasattr(self, 'p'):
            self.p.terminate()

    def get_diarized_transcript(self, audio_file_path, device="cpu", batch_size=16, compute_type="int8"):
        """
        Transcribes the given audio file and assigns speaker labels.
        Returns the transcript as a formatted JSON string.
        """
        # 1. Transcribe with original whisper (batched)
        model = whisperx.load_model("tiny", device, compute_type=compute_type)
        audio = whisperx.load_audio(audio_file_path)
        result = model.transcribe(audio, batch_size=batch_size, language='en')

        # 2. Align whisper output
        model_a, metadata = whisperx.load_align_model(language_code='en', device=device)
        result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

        # 3. Assign speaker labels
        diarize_model = whisperx.DiarizationPipeline(use_auth_token=self.huggingface_token, device=device)
        diarize_segments = diarize_model(audio)
        result = whisperx.assign_word_speakers(diarize_segments, result)

        # Clean up the output segments by removing unnecessary keys
        output = result["segments"]
        for segment in output:
            segment.pop('words', None)
            segment.pop('start', None)
            segment.pop('end', None)

        return json.dumps(output, indent=2)

    def record_audio(self):
        """
        Records audio until the user presses 'p' to stop the current session.
        The recording starts only if 'q' is not pressed.
        Returns the full file path and the audio file name.
        """
        # Wait for the user to start recording
        print("Waiting for recording trigger (press 'q' to cancel)...")
        while not keyboard.is_pressed('q'):
            # Begin recording when no cancellation signal is present
            print("Starting recording. Press 'p' to stop recording.")
            audio_frames = []
            stream = self.p.open(format=pyaudio.paInt16, channels=1,
                                rate=44100, input=True, frames_per_buffer=1024)
            # Record until 'p' is pressed
            while not keyboard.is_pressed('p'):
                data = stream.read(1024)
                audio_frames.append(data)
            print("Stopping recording...")
            stream.close()

            # Create a timestamped audio file
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            audio_file_name = f"{timestamp}.wav"
            sound_file_path = os.path.join(self.audio_directory, audio_file_name)

            # Write the audio frames to a wave file
            with wave.open(sound_file_path, "wb") as sound_file:
                sound_file.setnchannels(1)
                sound_file.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
                sound_file.setframerate(44100)
                sound_file.writeframes(b''.join(audio_frames))
            
            return sound_file_path, audio_file_name

    def process_audio(self):
        """
        Records audio and generates the diarized transcript,
        saving the transcript as a JSON file.
        """
        audio_file_path, audio_file_name = self.record_audio()
        transcript_json = self.get_diarized_transcript(audio_file_path)

        transcript_file_name = "transcript_" + audio_file_name.replace(".wav", ".json")
        transcript_path = os.path.join(self.transcript_directory, transcript_file_name)
        print(f"Saving transcript to {transcript_path}")

        with open(transcript_path, 'w') as transcript_file:
            transcript_file.write(transcript_json)

        print("Processing complete.")
        return transcript_path
    
    # Optionally, if you still need a stop_audio method, you can simplify it:
    def stop_audio(self):
        """Placeholder for stopping the audio process if needed."""
        print("Audio processing stopped (no multi-threading in this version).")

if __name__ == "main": 
    transcriber = AudioTranscriber() 
    transcriber.process_audio()
