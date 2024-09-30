import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime

# Initialize the TTS engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    query = None 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 320
        audio = r.listen(source, 0, 4)
        try:
            print("Understanding...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
        except Exception as e:
            try:
                # If English recognition fails, try recognizing in Hindi
                query = r.recognize_google(audio, language='hi-in')
                print(f"You said (in Hindi): {query}\n")
            except Exception as e:
                print("Say that again please...")
        return query

if __name__ == "__main__":
    while True:
        query = takeCommand()
        if query:
            query = query.lower()
            if "jarvis" in query or "utho jarvis" in query:
                from GreetMe import greetme
                greetme()

                while True:
                    query = takeCommand()
                    if query:
                        query = query.lower()
                        if "chalo bye" in query or "goodbye" in query:
                            speak("bye sir, you can call me anytime.")
                        elif "how are you" in query or "kaise ho" in query:
                            speak("Fine sir, how are you sir?")
                        elif "i am fine" in query or "main theek hun" in query:
                            speak("Perfect, sir.")
                        elif "thank you jarvis" in query:
                            speak("You are welcome, sir.")
                        elif "stop it " in query or "bakwas mat karo" in query:
                            speak(" sorry,sorry, boss ")
                        elif "are you mad" in query or "kya yaar Jarvis" in query:
                            speak(" sorry sir, aage se,nahi hoga, sir")

                        elif "youtube" in query:
                            from SearchNow import searchYoutube
                            searchYoutube(query)
                        elif "change the song" in query:
                            from SearchNow import searchYoutube
                            searchYoutube(query)

                        elif "google" in query:
                            from SearchNow import searchGoogle
                            searchGoogle(query)

                        elif "wikipedia" in query:
                            from SearchNow import searchWikipedia
                            searchWikipedia(query)

                        elif "temperature" in query:
                            search = "temperature in bhubaneswar"
                            url = f"https://www.google.com/search?q={search}"
                            r = requests.get(url)
                            data = BeautifulSoup(r.text, "html.parser")
                            temp = data.find("div", class_="BNeawe").text
                            speak(f"current{search} is {temp}")

                        elif "the current time" in query:
                            strTime = datetime.datetime.now().strftime("%H:%M")
                            speak(f"Sir, the time is {strTime}")

                        elif "open" in query or "open karo" in query:
                            from DictFile import openapp
                            openapp(query)

                        elif "close" in query or "close kar do" in query:
                            from DictFile import closeapp
                            closeapp(query)
