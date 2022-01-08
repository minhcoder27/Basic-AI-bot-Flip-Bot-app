
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
from function import *
wikipedia.set_lang('en')

friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 

diction_conversation = dict()

conversation(diction_conversation)

welcome()

while True:
    
    query=command().lower()
    
    if "google" in query:
        speak("What should I search,boss")
        search=command().lower()
        url = f"https://google.com/search?q={search}"
        wb.get().open(url)
        speak(f'Here is your {search} on google')   
    elif "youtube" in query:
        speak("What should I search,boss")
        search=command().lower()
        url = f"https://youtube.com/search?q={search}"
        wb.get().open(url)
        speak(f'Here is your {search} on youtube')
    elif query =="":
        speak("I can't here everything")
    elif "quit" in query:
        speak("Flip is off. Goodbye boss")
        quit()
    elif "bye" in query:
        speak("Flip is off. Goodbye boss")
        quit()
    elif "good bye" in query:
        speak("Flip is off. Goodbye boss")
        quit()
    elif 'what time' in query:
        time2()
    elif "let sing" in query:
        pygame.mixer.init()
        pygame.mixer.music.load("sing.mp3")
        pygame.mixer.music.play()
        time.sleep(20)
        pygame.mixer.music.pause()
    elif "can you sing" in query:
        speak("Yes, i can")
        pygame.mixer.init()
        pygame.mixer.music.load("sing.mp3")
        pygame.mixer.music.play()
        time.sleep(20)
        pygame.mixer.music.pause()
    elif "sing a song" in query:
        pygame.mixer.init()
        pygame.mixer.music.load("sing.mp3")
        pygame.mixer.music.play()
        time.sleep(20)
        pygame.mixer.music.pause()
    elif "do you know"  in query:
        text = query[query.find("know")+len("know"):]
        speak('Here is your'+ text + ' meaningg')
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
    elif "say about"  in query:
        text = query[query.find("about")+len("about"):]
        speak('Here is your'+ text + ' meaningg')
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        continue
    elif "tell about"  in query:
        text = query[query.find("about")+len("about"):]
        speak('Here is your'+ text + ' meaningg')
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        continue
    elif "pronoun" in query:
        text = query[query.find("pronoun")+len("pronoun")+3:]
        speak(text)
        print("FLip: ",ipa.convert(text))
        time.sleep(5)
    elif "translate" in query:
        text = query[query.find("translate")+len("translate")+1:]
        speak(text)
        translator = Translator()
        translated = translator.translate(text, src='en', dest='vi')
        speak_vn(translated.text)
        time.sleep(5)   
    elif "tell me about"  in query:
        text = query[query.find("about")+len("about"):]
        speak('Here is your'+ text + ' mean')
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        continue
    else:
        query = query.lower()
        if query in diction_conversation.keys():
            speak(diction_conversation[query])
        else:
            speak("I can't understand it")
            speak("Can you teach me? ")
            print("FLip: type <question>_<anwser>")
            query =str(input("You: ")).lower()
            fhand = open("conversation.txt","a")
            fhand.write("\n")
            fhand.write(query)
            fhand.close()
            fhand = open('conversation.txt','r')
            conversation(diction_conversation)

        