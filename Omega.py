from time import ctime
import speech_recognition as sr
import os
import webbrowser
from gtts import gTTS
import playsound


num = 1


# Creating Definition to convert text to speech


def omegaTalks(audio):
    global num

    # concat every audio file
    num += 1
    print("Omega : ", audio)

    toSpeak = gTTS(text=audio, lang='en-US', slow=False)
    # saving the audio file gtts
    file = str(num) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file
    playsound.playsound(file, True)
    os.remove(file)


# omegaTalks("Welcome User\n to Voice Assistant\n Created By Marcin Zawada Called Omega")


def omegaCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said: " + command)
        return command
    except sr.UnknownValueError:
        pass


def assistant(command):
    if command == 'open Wikipedia' or command == 'wiki' or command == 'Wikipedia' or command == 'open Viki':
        omegaTalks('ok')
        chrome_path = 'usr/bin/google-chrome'
        url = 'https://www.wikipedia.com/'
        webbrowser.open(url)

    elif command == 'open youtube' or command == 'open YouTube':
        omegaTalks('ok')
        chrome_path = 'usr/bin/google-chrome'
        url = 'https://www.youtube.com/'
        webbrowser.open(url)

    elif command == 'Google' or command == 'open Google' or command == 'Google':
        omegaTalks('ok')
        chrome_path = 'usr/bin/google-chrome'
        url = 'https://www.google.com/'
        webbrowser.open(url)
    elif command == 'what time is it' or command == 'Time' or command == 'time':
        omegaTalks(ctime())
    elif command == 'what is your name' or command == 'who are you' or command == 'What is your name':
        omegaTalks("My name is Omega, created by Marcin Zawada")
    elif command == 'Omega' or command == 'omega' or command == 'hey Omega':
        omegaTalks("I am ready for your command, Sir")



omegaTalks("What Can I Do For You?")
print("Listening...")
while True:
    assistant(omegaCommand())
