import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:

        speak("good afternoon")

    else:
        speak("good evening")

    speak("I am jarvis sir. please tell me how may i help you")
















