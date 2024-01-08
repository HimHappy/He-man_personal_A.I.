import speech_recognition as sr
import wikipedia as w
import openai as ai
import os
import pyttsx3
import webbrowser
import datetime
from utility import api_key

# def say(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
# if __name__ == '__main__':
#     say("Hello I'm Deceptron. A personal A.I. for my developer 'Happy'")

import win32com.client

website_keywords = ['open','go to','visit']
def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    # speaker.Rate = 0.8
    speaker.Speak(text)

def open_web(website):
    say(f"Opening {website} sir...")
    webbrowser.open(f"https://www.{website}.com")

def open_music():
    music_path1 = r'C:\Users\Administrator\Music\Pehle Bhi Main Tumse Mila Hu(PagalWorld.com.pe).mp3'
    music_path2 = r'C:\Users\Administrator\Music\O Mahi O Mahi(PagalWorld.com.pe).mp3'
    music_path3 = r'C:\Users\Administrator\Music\_Heeriye(PagalWorld.com.pe).mp3'
    # music_list = [music_path1,music_path2,music_path3]
    # say('i have ',len(music_list),' in my list, tell me the which one like 1, 2, 3')
    # TODO- get specific music input and play that song
    # TODO- search song
    say('Now playing music sir')
    # os.startfile(music_path1)
    os.startfile(music_path2)
    # os.startfile(music_path3)
    
def get_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    say(f"sir the time is {time}")

def chat(query):
    global chatStr
    print(chatStr)
    ai.api_key = api_key
    chatStr += f"Himanshu: {query}\n He-man: "
    response = ai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    ai.api_key = api_key
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = ai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def mic_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        global website_keywords
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        # audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='auto')
            print('Recognized: {}'.format(text))
            if 'exit' in text.lower() or 'sleep' in text.lower():
                say("Going to Sleep. See you soon!")
                exit()
            # elif 'open' in text.lower() and 'website' in text.lower():
            #     website = text.lower().replace("open","").replace("website","").strip()
            #     say(f"Opening {website} sir...")
            #     webbrowser.open(f"https://www.{website}.com")
            elif any(keyword in text.lower() for keyword in website_keywords):
                keyword = next(keyword for keyword in website_keywords if keyword in text.lower())
                index_keyword = text.lower().index(keyword)
                wesite_name_start = index_keyword+len(keyword)
                website = text[wesite_name_start:].split()[0].strip()
                # ToDo: write code to split .com .in .net .org .edu like that
                open_web(website)
            # elif '.com' in text.lower():
            #     say(f"Opening {website} sir...")
            #     website = text.replace('open','').split()[0].strip()
            #     webbrowser.open(f"https://www.{website}")
            elif 'play music' in text.lower():
                open_music()
            elif 'time' in text.lower():
                get_time()
            elif "Using artificial intelligence".lower() in text.lower():
                ai(prompt=text)
            else:
                say(text)
        except sr.UnknownValueError:
            print('Could not understand audio')
            return say("Sorry, could you please repeat?")
        except sr.RequestError as e:
            # This error can occur if Google Speech Recognition is not installed or functioning properly
            print('Google Speech Recognition could not understand the audio')
            return say("Sorry, could you please repeat?")

if __name__ == '__main__':
    say("Hello my name is He-man. A personal A.I. of my developer 'Himanshu'. how can i help you today")
    # say("if you want to open some website, please don't use .com .net or something ending with a dot. Just tell me like open or go to or visit and website name. Thanks")
    while True:
        text = mic_input()