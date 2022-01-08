from re import S
import eng_to_ipa as ipa
import pyttsx3
import pyaudio
import PyInstaller
import datetime 
import speech_recognition as sr
import webbrowser as wb
import wikipedia
import time
import pygame
import random
import telegram
from googletrans import Translator
from gtts import gTTS
friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 

def speak(audio):
    print('Flip: ' + audio)
    friday.say(audio)
    friday.runAndWait()


def speak_vn(text):
    print("Flip: {}".format(text))
    tts = gTTS(text, lang="vi", slow=False)
    name_file = str(random.random()) + "sound.mp3"
    tts.save(name_file)
    pygame.mixer.init()
    pygame.mixer.music.load(name_file)
    pygame.mixer.music.play()

    
def time2():
    Time=datetime.datetime.now().strftime("%I:%M:%p") 
    speak("It is")
    speak(Time)

def welcome():
        hour=datetime.datetime.now().hour
        if hour >= 6 and hour<12:
            speak("Good Morning Sir!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon Sir!")
        elif hour>=18 and hour<24:
            speak("Good Evening sir")
        else:
            speak("oh! Good Midnight sir, so late now")
        speak("How can I help you,boss") 
s=0
def command():
    print("FLip: ...")
    query = None
    c=sr.Recognizer()
    with sr.Microphone() as source:
        audio=c.record(source,duration= 3)
    try:
        query = c.recognize_google(audio,language='en-US')
        print("You: "+query)
    except sr.UnknownValueError:
        query =""
        
    return query
def conversation(diction_conversation):
    fhand = open('conversation.txt','r')
    s ="0"
    data_list = fhand.readlines() 
    for i in range(len(data_list)):  
        line = str(data_list[i]) 
        line = line.rstrip()
        line = line.rstrip('\r\n')
        line = line.lower()
        pair_key_val = line.split('_')
        diction_conversation[pair_key_val[0]] = pair_key_val[1]

