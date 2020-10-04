from datetime import datetime
import pyttsx3
import speech_recognition as sr

# function for voice response of jarvis
def speak(str):
    engine=pyttsx3.init()
    engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    engine.say(str)
    engine.runAndWait()

# function for listening commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.threshold=0.7
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        command = r.recognize_google(audio,language='en-in')
        print(f"User said: {command}")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return 'None'
    return command

# greeting according to the time of day
def wish():
    hour=datetime.now().hour
    if hour>=3 and hour<=12:
        speak("very good morning sir!!!")
    elif hour>=17 or hour<3:
        speak("very good evening sir!!!")
    elif hour>12 and hour<17:
        speak("very good afternoon sir!!!")

# actual body of the jarvis performing logical tasks
if __name__=="__main__":
    wish()
    while True:

        said = takeCommand().lower()    # listening command from users
        
        if "time" in said:
            hr=datetime.now().strftime('%H:%M:%S').split(":")
            print(f"{hr[0]} hour {hr[1]} minute")
            speak(f"{hr[0]} hour {hr[1]} minute")
        elif "news" in said:
            import requests
            import json
            from random import randint
            url="https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=d28f42cd05fe4d7c8e15de818cd9d5f8"
            page=requests.get(url)
            text=page.text
            news=json.loads(text)
            articles=news["articles"]
            print(articles[randint(0,len(articles)-1)]['title'])
            speak(articles[randint(0,len(articles)-1)]['title'])
        elif "developed you" in said:
            speak("Mr. GYanendra DAS")
        elif 'exit' in said:
            print("Jarvis is shutting down")
            speak("Jarvis is shutting down")
            exit()
        else:
            print('I didn\'t understood Sir. Should i search wikipedia.')
            speak('I didn\'t understood Sir. Should i search wikipedia.')
            print('Please say yes or no')
            speak('Please say yes or no')
            said = takeCommand().lower()
            if 'yes' in said:
                import wikipedia
                search=wikipedia.summary(said,sentences=1)
                print(f"according to my master lucky........{search}")
                speak(f"according to my master lucky........{search}")
            else:
                continue

