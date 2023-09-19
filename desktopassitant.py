import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source,duration=5)
        print('Ask me anything..')
        recordedaudio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

    except Exception as ex:
        print(ex)

    if 'chrome' in text:
        a='Opening chrome..'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    if 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'play' in text:
        a='opening youtube..'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    if 'youtube' in text:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com/')
    if 'hotstar' in text:
        b='opening hotstar'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.hotstar.com/in')
    if 'netflix' in text:
        b='opening netflix'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.netflix.com/in')
    if 'open prime' in text:
        b='opening primevideo'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.primevideo.com/')
    if 'open netflix latest' in text:
        b='opening netflix trendings'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.netflix.com/in/browse/genre/839338')
    if 'open news' in text:
        b='opening trending news'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR000ZEdzU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen')
    if 'open music' in text:
        b='opening trending music'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://open.spotify.com/playlist/37i9dQZF1DXbVhgADFy3im')
    if 'love today songs' in text:
        b='opening love today songs'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://youtu.be/R3w8u-38-Eo')
    if 'sec' in text:
        b='here is saveetha engineering college'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.saveetha.ac.in/')
    

while True:
    cmd()
