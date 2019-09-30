from datetime import datetime
def speak(str):
    import pyttsx3
    engine=pyttsx3.init()
    engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    engine.say(str)
    engine.runAndWait()

    
def wish():
    hour=datetime.now().hour
    if hour>=3 and hour<=12:
        speak("very good morning sir!!!")
    elif hour>=17 or hour<3:
        speak("very good evening sir!!!")
    elif hour>12 and hour<17:
        speak("very good afternoon sir!!!")


if __name__=="__main__":
    wish()
    while True:
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.threshold=0.7
            audio=r.listen(source)
        print("Recognizing.....")
        said=r.recognize_google(audio,language='en-in')
        if "time" in said:
            hr=datetime.now().strftime('%H:%M:%S').split(":")
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
            speak(articles[randint(0,len(articles)-1)]['title'])
        elif "developed you" in said:
            speak("Mr. GYanendra DAS")
        else:
            import wikipedia
            search=wikipedia.summary(said,sentences=1)
            speak(f"according to my master lucky........{search}")


        

