import pyttsx3
import pyautogui
import webbrowser
import os
import subprocess
from difflib import get_close_matches as find
from os import system

# Initialize the TTS engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def openapp(query):
    if "open" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("please", "")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.sleep(0)
        pyautogui.press("enter")
        pyautogui.press("enter")

def closeapp(query):
    program = []
    progid = []
    progdict = {}

    for i in range(0, len(progid)):
        progdict[program[i]] = progid[i]

    def close(c):
        global program, progid, progdict
        q = find(c, program)
        if q == []:
            speak("app is not found to close")
        else:
            for key, value in progdict.items():
                if key == q[0]:
                    speak(f"{key} is closing")
                    system("taskkill /im  " + str(value))