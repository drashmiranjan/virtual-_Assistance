import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning,sir")
    elif hour>12 and hour<=15:
        speak("Good Afternoon,sir")
    else:
        speak("Good Evening,sir")

    speak("How can i help you,sir")

