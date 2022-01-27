import webbrowser
import speech_recognition as sr
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime


r = sr.Recognizer()


def speech_recognition(ask = False):
    with sr.Microphone() as speech:
        if ask:
            java_speak(ask)
        java_speak("Speak : ")
        audio = r.listen(speech)
        StoredSpeech = ''
        try:
            StoredSpeech = r.recognize_google(audio)
        except sr.UnknownValueError:
            java_speak("Sorry could not hear properly")
        except sr.RequestError:
            java_speak("Sorry I am down")
        return StoredSpeech


def java_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000000)
    audio_file = 'audio-' + str(r) + 'mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def reply(StoredSpeech):
    if ("exit" or "stop" or "break") in StoredSpeech:
        exit()
    if StoredSpeech == "hello":
        java_speak("Walaikum Asalaam")
    if StoredSpeech == "hi":
        java_speak("Walaikum Asalaam")
    elif StoredSpeech == "what is your name":
        java_speak("My name is Java")
    elif StoredSpeech == "who is your master" or StoredSpeech == "who created you":
        java_speak("Master Faizan")
    elif "what time is it" in StoredSpeech:
        java_speak(ctime())
    elif "find location" in StoredSpeech:
        location = speech_recognition('Which location you want to search for? ')
        url = 'https://www.google.com/maps/place/'+location+'/&amp;'
        webbrowser.get().open(url)
        print("Here is your location" + location)
    elif "search" in StoredSpeech:
        searched = speech_recognition('What do want to search for? ')
        url = 'https://www.google.com/search?'+searched
        webbrowser.get().open(url)
        print("Here is your search " + searched)

time.sleep(1)
while 1:
    StoredSpeech = speech_recognition()
    reply(StoredSpeech)
