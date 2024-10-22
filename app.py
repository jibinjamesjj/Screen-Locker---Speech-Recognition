import speech_recognition as sr
from gtts import gTTS
import os
import subprocess
import pyttsx3

recognizer = sr.Recognizer()

language = 'en'
cmd='rundll32.exe user32.dll, LockWorkStation'

try:
    # List available microphones (optional)
    #print("Available microphones:")
    #print(sr.Microphone.list_microphone_names())

    # Select a specific microphone (optional)
    # with sr.Microphone(device_index=1) as source:

    with sr.Microphone(device_index=2) as source:
        print("Adjusting noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording for 10 seconds...")
        recorded_audio = recognizer.listen(source, phrase_time_limit=3)
        print("Done recording.")

        print("Recognizing the text...")
        mytext = recognizer.recognize_google(recorded_audio, language="en-US")
        print("Decoded Text: {}".format(mytext))

        if mytext == "lock the screen":
            subprocess.call(cmd)
        #myobj = gTTS(text=mytext, lang=language, slow=False)
        #myobj.save("welcome.mp3")
        #os.system("start welcome.mp3")
        #subprocess.call(cmd)

        engine = pyttsx3.init()
        engine.say("You said" + mytext)
        engine.runAndWait()

except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
except Exception as ex:
        print("Error during recognition:", ex)