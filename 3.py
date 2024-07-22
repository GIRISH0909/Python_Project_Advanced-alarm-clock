import speech_recognition as sr
import subprocess
import pyttsx3


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noises..')
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('ask me anything..')
        recordedaudio=recognizer.listen(source)

    try:
        print('printing your message....')
        command=recognizer.recognize_google(recordedaudio,language='en-US')

    except Exception as ex:
        print(ex)


    if 'chrome' in command:
        a='opening chrome..'
        engine.say(a)
        engine.runAndWait()
        program="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])
