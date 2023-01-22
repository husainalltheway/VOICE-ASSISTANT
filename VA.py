#pyttsx3 will help to convert text into speech
import pyttsx3
#this will help to recognize your voice
import speech_recognition as sr
#this will help you to browse through the browser
import webbrowser
#this will help you to ask for date or time or to check how much did any command took to get complete
import datetime
#this will give some jokes
import pyjokes

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise (source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Pardon !!")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',140)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    #if sptext().lower() == "hey jazz" :
        while True:
            data1 = sptext().lower()
            
            if "your name " in data1:
                name = "my name is veronica"
                speechtx(name)

            elif "old are you" in data1:
                age = "i am twenty years old"
                speechtx(age)

            elif "how are you" in data1:
                how = "I am fine, how are you ?"
                speechtx(how)

            elif "now time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)

            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            
            elif "google" in data1:
                webbrowser.open("https://www.google.com/")

            elif "joke" in data1:
                jokes = pyjokes.get_joke(language= "eng",category="neutral")
                speechtx(jokes)
                print(jokes)

            elif "go have some rest" in data1:
                speechtx("as you say....")
                break
    #else:
        #print("thanks")