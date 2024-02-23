import os
import playsound
import pyautogui
import speech_recognition as sr
import datetime
import webbrowser
from gtts import gTTS
import pyttsx3
import win32com.client
import openai
from config import apikey


def say(text):
    speaker = win32com.client.Dispatch("SAPI.spvoice")
    speaker.Speak(text)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5  # it shows how many time jarvis take
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry sir"

if __name__ == '__main__':
    print('Welcome sir i am jarvis')
    say("hi sir i am jarvis jay shree raamm")
    #This while loop infinity jae listening karibi
    while True:
        print("Listening...")
        text = get_audio()

        # This command is used for opening youtube .lower convert the text in to lower case
        if "Open youtube jarvis" .lower() in text.lower():
            say("opening youtube sir")
            webbrowser.open("https://www.youtube.com")

        # This command is used for opeaning linked in
        if "open linkedin jarvis".lower() in text.lower():
            say("opening linkedin sir")
            webbrowser.open("https://www.linkedin.com/feed/")

        # This command is used for opeaning my song

        if "jarvis play song" .lower() in text.lower():
            say("Alright sir opening")
            webbrowser.open("https://www.youtube.com/watch?v=x6Q7c9RyMzk")
        if "play next jarvis".lower() in text.lower():
            say("playing next")
            webbrowser.open("https://www.youtube.com/watch?v=22bLNq6iCjU&list=RDdXl2NdlmeIE&index=4")

        # This command is used for paly a music from downloads
        if "play music" in text:
            musicPath = "D:\programming\MyAI\leosong.mp3"
            say("okay sir playing")
            os.startfile(musicPath)
        if "next" in text:
            say("playing next music sir")
            musicpath = "D:\programming\MyAI\kolavari.mp3"
            os.startfile(musicpath)

        # TO show the Time and date to do This we should Import Date and Time
        if "what is the time" in text:
            # srtf file is a function which give the accurate time and date as per our Desktop
            strfile = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Time Hai {strfile}")

        # To open an desktop app By Gven command to jarvis
        if "open" in text:
            text = text.replace("open","")
            text = text.replace("jarvis","") # it replace or remove the jarvis
            pyautogui.press("super")  #pyautogui is a packag through we can open any application from our desktop
            pyautogui.typewrite(text) #pyauyogui is taking acess of our keyboard
            say(f"opening {text} sir")
            pyautogui.press("enter")

        # # It quit the the the terminal and keave from the command
        # elif "Jarvis Quit".lower() in text.lower():

        #     exit()
        #
        # # It reset the chat (chat ku start ru start kariba)
        # elif "reset chat".lower() in text.lower():
        #     chatStr = ""











