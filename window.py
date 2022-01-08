from tkinter import *
from PIL import Image,ImageTk
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

diction_conversation = dict()

fhand = open('conversation.txt','r')
data_list = fhand.readlines() 
for i in range(len(data_list)):  
    line = str(data_list[i]) 
    line = line.rstrip()
    line = line.rstrip('\r\n')
    line = line.lower()
    pair_key_val = line.split('_')
    diction_conversation[pair_key_val[0]] = pair_key_val[1]

#tạo window
root = Tk()
root.title("Flip Bot")
root.geometry("500x630")
root.iconbitmap("logo.ico")

load=Image.open("background.png")
render = ImageTk.PhotoImage(load)
img = Label(root,image=render)
img.place(x=0,y=0)

name=Label(root,text="FLIP BOT",fg="#FFFFFF",bd=0,bg="#03152D")
name.config(font=("Transformers Movie",30))
name.pack(pady=10)

box = Text(root,width=28,height=8,font=("ROBOTO",16))
box.pack(pady=20)

but_fr=Frame(root).pack(side=BOTTOM)
def speak(audio):
    box.delete(1.0,END)
    box.insert(END,"Flip: "+audio)
    friday.say(audio)
    clear_but = Button(but_fr,text="clear text",font=(("Arial"),10,'bold'),bg ="#303030",fg="#FFFFFF")
    clear_but.place(x=150,y=310)
    start_but = Button(but_fr,text="open",font=(("Arial"),10,'bold'),bg ="#303030",fg="#FFFFFF",)
    start_but.place(x=290,y=310)
    box1 = Text(root,width=28,height=8,font=("ROBOTO",16))
    box1.pack(pady=50)
    friday.runAndWait()
def speak_vn(text):
    box.delete(1.0,END)
    box.insert(END,"Flip: {}".format(text))
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
    c=sr.Recognizer()
    with sr.Microphone() as mic:
        audio=c.record(mic, duration= 3)
    try:
        query = c.recognize_google(audio,language='en-US')
        print("You: " + query)
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command')
        query = str(input("You: "))
        
    return query
def run():

    welcome()

    while True:
    
        print("Flip:...")
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
        elif "where do you live" in query:
            speak("I live on your device")
        elif "where do you from" in query:
            speak("I live on your device")
        elif "how old are you" in query:
            speak("I'm 1 month years old")
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
        elif "what's your name" in query:
            speak("My name is FLip")
        elif "how do you spell your name" in query:
            speak("F,L,I,P")
        elif "do you love Vietnam" in query:
            speak("yes of course, because it is country of my father")
        elif "do you like Vietnam" in query:
            speak("yes of course, because it is country of my father")
        elif "what is your father" in query:
            speak("my father is Tan Minh")
        elif "what's your father" in query:
            speak("my father is Tan Minh")
        elif "how are you" in query:
            speak("i'm ok")
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
                data_list = fhand.readlines() 
                for i in range(len(data_list)):  
                    line = str(data_list[i]) 
                    line = line.rstrip()
                    line = line.rstrip('\r\n')
                    line = line.lower()
                    pair_key_val = line.split('_')
                    diction_conversation[pair_key_val[0]] = pair_key_val[1]

        
clear_but = Button(but_fr,text="clear text",font=(("Arial"),10,'bold'),bg ="#303030",fg="#FFFFFF")
clear_but.place(x=150,y=310)
start_but = Button(but_fr,text="open",font=(("Arial"),10,'bold'),bg ="#303030",fg="#FFFFFF",command=run())
start_but.place(x=290,y=310)
box1 = Text(root,width=28,height=8,font=("ROBOTO",16))
box1.pack(pady=50)
speak("hello")
root.mainloop()



