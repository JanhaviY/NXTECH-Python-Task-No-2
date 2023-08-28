import speech_recognition as sr
from time import ctime 
import time 
import pyaudio
import webbrowser
import playsound
import os
import random
from gtts import gTTS


# Initialize the recogniser to recognise the speech
s = sr.Recognizer()

def record_audio(ask = False):
# Whatever we speak will reach via the microphone
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio= s.listen(source)
        voice_data = ''
        try:
            voice_data = s.recognize_google(audio)
        except sr.UnknownValueError:
            alexa_speak("Sorry, I did not get that.")
        except sr.RequestError:
            alexa_speak("Sorry my speech service is down.")
        return voice_data

# Define a function for text to speech conversion   
def alexa_speak(audio_string):
    tts = gTTS(text=audio_string,lang="en")
    r = random.randint(1,10000000)
    audio_file = "audio-" +str(r)+ '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
        if "what is your name" in voice_data:
            alexa_speak("My name is Alexa.")
        if "what time is it" in voice_data:
            alexa_speak(ctime())
        if "search" in voice_data:
            search = record_audio("what do you want to search?")
            url = "https://google.com/search?q" + search 
            webbrowser.get().open(url)
            alexa_speak("Here is what I found for"+ search)
        if "find location" in voice_data:
            location = record_audio("what is the location?")
            url = "https://google.nl/maps/place/" + location + "/&amo" 
            webbrowser.get().open(url)
            alexa_speak("Here is the location of" + location)
        if "open video" in voice_data:
            video = record_audio("Which video do you want to see?")
            url = "https://www.youtube.com/watch?v/" + video + "/&pp=sAQA"
            webbrowser.get().open(url)
            alexa_speak("youtube video you asked for is available : " + video)
        if "exit" in voice_data:
            exit()

time.sleep(1)
alexa_speak("How can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)