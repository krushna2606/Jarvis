import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("I am Jarvis. Please tell me what can I do for you")            

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")   

    except Exception as e:
         # print(e)
        speak("Say that again please...")
        return "None"
    return query    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com', 'yourpassword')
    server.sendmail('yourmail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


        if 'search' in query:
            speak('Searching on memory...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("Sir according to my knowledge")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Sir,opening youtube..")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Sir,opening google..")
            webbrowser.open("google.com") 

        elif 'open facebook' in query:
            speak("Sir,opening Facebook..")
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            speak("Sir,opening instagram..")
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            path = r"dir path"
            song = random.choice(os.listdir(path))
            speak("Sir,your music..")
            os.startfile(path+'\\'+song)

        elif 'watch movies' in query:
            movies_dir = 'dir pth'
            movies = os.listdir(movies_dir)
            print(movies)
            os.startfile(os.path.join(movies_dir, movies[0]))
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")    
            
        elif 'open code' in query:
            codePath = "dir path"
            os.startfile(codePath)

        elif 'email to name' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "recievers@gmail.com"
                sendEmail(to, content)
                speak("Your Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir your Email is failed to send!")

        elif 'email to name' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "recievers@gmail.com"
                sendEmail(to, content)
                speak("Your Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir your Email is failed to send!")

        elif 'email to name' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "recievers@rediffmail.com"
                sendEmail(to, content)
                speak("Your Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir your Email is failed to send!")

        elif 'email to name' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "recievers@gmail.com"
                sendEmail(to, content)
                speak("Your Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir your Email is failed to send!")        

            


        

           

        
