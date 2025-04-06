import os
import speech_recognition as sr
import keyboard
import datetime


def RecordTranscript():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_vosk(audio)
    except sr.UnknownValueError:
        print("Vosk could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Vosk service; {e}")

recognizer = sr.Recognizer()
# We can use this to increase the cutoff noise level if we are in a loud room
#recognizer.energy_threshold = 4000

# Adjusts how long you have to be silent for before cutting off recording
#recognizer.pause_threshold = 0.8  # type: float

start_pressed = False
file_notes_path = 'user_notes/'
print("nPress Spacebar to record.\n")
while (1):

    while(start_pressed == False):
        if keyboard.is_pressed('space'):
            raw_transcript = RecordTranscript()
            raw_transcript_path = os.path.join(file_notes_path, "raw_transcripts")

            file_name = str(datetime.datetime.now()).strip(' ')
            file_name = file_name[:len(file_name)-7].replace(":", "_") + ".json"
            with open(os.path.join(raw_transcript_path,file_name), 'w') as new_transcript_file:
                new_transcript_file.write(raw_transcript)

            print("\nDone Recording!\nPress Spacebar to record again.\n")
