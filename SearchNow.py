import random

import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit

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
        r.energy_threshold = 300
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

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found on Google")
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)
        except:
            speak("Sorry, I couldn't find anything on the internet")

def searchYoutube(query):
    try:

        if "youtube" in query:
            speak("This is what I found for your search!")
            query = query.replace("youtube search", "")
            query = query.replace("youtube", "")
            query = query.replace("jarvis", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Done, Sir")
            if "change the song" in query:
                # web.pause()
                web = "https://www.youtube.com/watch?v=" + query
    except sr.RequestError as e:
        print(f"Could not request results; {e}")


def searchWikipedia(query):
   if "wikipedia" in query:
       speak("This is what i Found for you, sir!")
       query = query.replace("wikipedia search", "")
       query = query.replace("wikipedia", "")
       query = query.replace("jarvis", "")
       query = query.replace("search karo", "")
       results = wikipedia.summary(query, sentences=1)
       speak("According to wikipedia..")
       print(results)
       speak(results)