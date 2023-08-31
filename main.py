import random

import win32com.client
import speech_recognition as sr
import webbrowser
import datetime
import os
import openai
from config import apikey
import random

openai.api_key = apikey

speaker=win32com.client.Dispatch("SAPI.SpVoice")

def ai(prompt):
    openai.api_key = apikey
    text=f"Open ai response for {prompt}\n\n**************\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text+=response["choices"][0]["text"]
    print(response["choices"][0]["text"])
    if not os.path.exists("openai"):
        os.mkdir("openai")
    with open(f"openai/prompt- {random.randint(1,2131222123)}","w") as f:
        f.write(text)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 0.6
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query =  r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e:
            return "Some Error Occurred"
if __name__=='__main__':


    speaker.Speak("Hello I am VJ AI")
    while 1:
        #print("Enter the speech you want to say it through computer : ")
        #s=input()

        print("Listening...")
        text=takeCommand()
        sites=[["youtube","https://youtube.com"],["google","https://google.com"],["wikipedia","https://wikipedia.com"],["yahoo","https://yahoo.com"]]
        for site in sites:
            if(f"Open {site[0]}").lower() in text.lower():

                speaker.Speak(f"Opening {site[0]} sir..")
                webbrowser.open(site[1])
        '''if "open music" in text:
            musicpath="Users/cnvadiraj/Downloads/downfall-21371.mp3"
            os.system(f"open {musicpath}")'''
        if "the time" in text:
            strfTimeh=datetime.datetime.now().strftime("%H")
            strfTimem = datetime.datetime.now().strftime("%M")
            strfTimes = datetime.datetime.now().strftime("%S")

            speaker.Speak(f"Sir the time is{strfTimeh} hours {strfTimem} minutes {strfTimes} seconds")
        if "open chrome".lower() in text.lower():
            os.system("start chrome")
        if "Using artificial intelligence".lower() in text.lower():
            ai(prompt=text)



        #speaker.Speak(text)