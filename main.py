import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import pyttsx3
import datetime
import random
import subprocess

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************************\n\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "write a email to boss for resignation?"
            },
            {
                "role": "assistant",
                "content": "Subject: Resignation Letter\n\nDear [Boss's Name],\n\nI hope this email finds you well. After giving thorough consideration to my professional journey and personal goals, I have made the difficult decision to resign from my position at [Company Name], effective [last"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0

    )
    #todo: grap inside of a try catch black
    print(response["choices"][0]["text"])
    text+= response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:])}.txt","w") as f:
        f.write(text)


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    os.system(f'say "{text}"')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing.........")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('PyCharm')
    say('Hello Unilesh')
    while True:
        print("Listening....")

        query = takeCommand()

        if "Using artificial intelligence" in query.lower():
            prompt = "Ask Jarvis: " + query  # You can customize the prompt here
            ai(prompt)
            # The ai() function will generate an OpenAI response for the given prompt.


        import webbrowser

        query = takeCommand()
        # todo: Add more sites

        sites = [["youtube", "https://www.youtube.com/"],
                 ["wikipedia", "https://www.wikipedia.org/"],
                 ["Bard", "https://bard.ai/"],
                 ["google", "https://www.google.com/"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                break  # Optionally, you can add a break statement to exit the loop after opening the website.
            #todo: Add a feature to play a specific song
            if "open music" in query:
                musicPath = "C:/Users/disha/Downloads/tvari-hawaii-vacation-159069.mp3"
                os.startfile(musicPath)
            if "the time" in query:
                hour = datetime.datetime.now().strftime("%H")
                minute = datetime.datetime.now().strftime("%M")
                say(f"Mam, the time is {hour}:{minute}.")

        def open_vscode():
            vs_code_path = r"C:\Users\disha\Downloads\VSCodeUserSetup-x64-1.79.2 (1).exe"
            os.startfile(vs_code_path)
        if "open VS Code" .lower() in query.lower():
            os.system(f"C:/Users/disha/OneDrive/Desktop/Visual Studio Code.lnk")
        if "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        #say(text)
