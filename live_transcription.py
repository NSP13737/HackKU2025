import os
import whisperx
import keyboard
import datetime
import pyaudio
import wave


def getDiarizedTranscript(audio_file_path):

    device = "cpu"
    batch_size = 16 # reduce if low on GPU mem
    compute_type = "int8" # change to "int8" if low on GPU mem (may reduce accuracy)

    # 1. Transcribe with original whisper (batched)
    model = whisperx.load_model("tiny", device, compute_type=compute_type)

    audio = whisperx.load_audio(audio_file_path)
    result = model.transcribe(audio, batch_size=batch_size, language='en')
    #print(result["segments"]) # before alignment

    # delete model if low on GPU resources
    # import gc; gc.collect(); torch.cuda.empty_cache(); del model

    # 2. Align whisper output
    model_a, metadata = whisperx.load_align_model(language_code='en', device=device)
    result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

    #print(result["segments"]) # after alignment

    # delete model if low on GPU resources
    # import gc; gc.collect(); torch.cuda.empty_cache(); del model_a

    # 3. Assign speaker labels
    diarize_model = whisperx.DiarizationPipeline(use_auth_token="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", device=device)

    # add min/max number of speakers if known
    diarize_segments = diarize_model(audio)
    # diarize_model(audio, min_speakers=min_speakers, max_speakers=max_speakers)

    result = whisperx.assign_word_speakers(diarize_segments, result)

    for key, value in result.items():
        #print(f"Key: {key}, Value: {value}\n")
        continue

    output = result["segments"]
    for i in range(len(output)):
        output[i].pop('words')

    return output # segments are now assigned speaker IDs




def recordAudio(audio_base_path):
    # Ensure the directory exists
    os.makedirs(audio_base_path, exist_ok=True)

    while(keyboard.is_pressed('q') == False):

        print("Starting recording")
        audio_frames = []
        current_stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        # Stop recording when user presses p
        while (keyboard.is_pressed('p') == False):
            data = current_stream.read(1024)
            audio_frames.append(data)
        print("Stopping recording")
            
        #current_stream.stop_stream() #pauses recording
        current_stream.close() #stops recording

        # Create a file for the audio
        timestamp = str(datetime.datetime.now())
        audio_file_name = timestamp[:len(timestamp)-7].replace(":", "_") + ".wav"
        
        sound_file_path = os.path.join(audio_base_path, audio_file_name)
        sound_file = wave.open(sound_file_path, "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b''.join(audio_frames))
        sound_file.close()

        return sound_file_path, audio_file_name
    
    
    
    
    
    
    
    
    
    
    
    
AUDIO_DIRECTORY = 'user_notes/audio'
TRANSCRIPT_DIRECTORY = 'user_notes/transcripts'

p = pyaudio.PyAudio()

while (1):
    if keyboard.is_pressed('space'):
        audio_base_path = os.path.join(os.getcwd(), AUDIO_DIRECTORY)
        audio_file_path, audio_file_name = recordAudio(audio_base_path)

        # Now we run audio through whisper
        transcript_file_name = "transcript_" + audio_file_name.replace(".wav", ".json")
        with open(os.path.join(TRANSCRIPT_DIRECTORY, transcript_file_name), 'w') as transcript:
            print(f"Opening {transcript}")
            transcript_dict = getDiarizedTranscript(audio_file_path)
            for segment in transcript_dict:
                transcript.write(str(segment)+"\n")
            


p.terminate()
