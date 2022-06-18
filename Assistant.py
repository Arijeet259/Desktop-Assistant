from http import server
from logging import exception
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
import pyaudio
import pywhatkit
print("Welcome!!")
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)    
def speak(text):
    engine.say(text)
    engine.runAndWait()
def greet():
    hr=datetime.datetime.now().hour
    if hr>=0 and hr<12:
        speak("Good Morning! ")
    elif hr>=12 and hr<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
speak("This is your desktop assistant!! what can i do for you")
# def commands():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listning..")
#         audio=r.listen(source)
#     try :
#         query=r.recognize_google(audio , Language='en-in')
#         print(f"you said: {query}\n")
#     except Exception as e:
#         print("please say that again")
#         query=None
#     return query
def sendEmail(username,password,to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(username,to,content)
    server.close()
greet()
speak("what can i do for you")
q=input("search ")
if 'wikipedia' in q.lower():
    print("searching..")
    speak('searching..')
    q=q.replace("wikipedia","")
    res=wikipedia.summary(q,sentences=2)
    print(res)
elif 'youtube' in q.lower():
    webbrowser.open("youtube.com")
elif 'vscode' in q.lower():
    codepath="C:\\Users\\arije\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codepath)
elif 'leetcode' in q.lower():
    webbrowser.open("https://leetcode.com/problemset/all/")
elif 'message' in q.lower():
    hr=int(input("enter thr hour: "))
    min=int(input("enter the minute: "))
    num=input("enter the number to which message will be send:")
    text=input("enter the message:")
    pywhatkit.sendwhatmsg(f'+91{num}',text,hr,min)
elif 'justcause3' in q.lower():
    os.startfile("D:\\Just Cause 3\\JustCause3.exe")
elif 'email' in q.lower():
    try:
        usrnm=input("username: ")
        passwrd=input("password: ")
        to=input("who to send: ")
        contnt=("what to send:")
        sendEmail(usrnm,passwrd,to,contnt)
        print("emai sent")
    except:
        print("error")