import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptxt():
    while True:
        recognizer=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                print("Recognizing...")
                data = recognizer.recognize_google(audio)
                return data
                print(data)
                break
            except sr.UnknownValueError:
                print("Not Recognizable")


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    if "nexa" in sptxt().lower():
        while True:
            data1 = sptxt().lower()

            if "your name" in data1:
                name = "My name is Nexa"
                speechtx(name)

            elif "old are you" in data1:
                age = "age is just a number! but if you're curious, i'm young at heart and wise beyond my algorithms!"
                speechtx(age)

            elif "colour of sky" in data1:
                sky = "blue"
                speechtx(sky)

            elif 'time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)

            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")

            elif 'google' in data1:
                webbrowser.open("https://www.google.com/")

            elif 'instagram' in data1:
                webbrowser.open("https://www.instagram.com/")

            elif 'gmail' in data1:
                webbrowser.open("https://mail.google.com/")

            elif 'github' in data1:
                webbrowser.open("https://github.com/IshanBhagwat")

            elif 'spotify' in data1:
                webbrowser.open("https://www.spotify.com/")

            elif 'twitter' in data1:
                webbrowser.open("https://x.com/")

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                speechtx(joke_1)

            elif 'play song' in data1:
                add = 'C:\\Users\\bhagw\\OneDrive\\Desktop\\songs'
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add,listsong[0]))

            elif 'exit' in data1:
                speechtx("thanks for chatting! if you ever need me again, just give me a shout. have a fantastic day!")
                print("Thank you for using our service! I hope I was able to assist you today. If you have any more questions in the future, feel free to reach out. Have a great day!")
                break

            time.sleep(3)

    else:
        speechtx("Say my name")
