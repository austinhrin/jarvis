# preinstalled python dependancies
from datetime import datetime
import re
#import smtplib # will allow you to send emails

# pip installed dependancies
#import wolframalpha
import wikipedia
import pyttsx3
import speech_recognition as sr
#import geckodriver_autoinstaller #https://pypi.org/project/geckodriver-autoinstaller/
#import chromedriver_autoinstaller #https://pypi.org/project/chromedriver-autoinstaller/

# user created dependancies
from config import MASTER, tts_voice_rate
from modules.open import open_url
from modules import volume

# initial variables
#wolf = wolframalpha.Client("")
# text to speech
tts = pyttsx3.init('sapi5')
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[0].id)
tts.setProperty('rate',tts_voice_rate)


def speak(text):
    tts.say(text)
    tts.runAndWait()

def greet_master():
    hour = int(datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good morning ' + MASTER)
    elif hour >= 12 and hour < 18:
        speak('Good afternoon ' + MASTER)
    else:
        speak('Good evening ' + MASTER)


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language = 'en-us')
        print(f'You said {query}\n')
    except Exception as e:
        print('nothing was said')
        query = None
    return query

'''
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('@gmail.com', 'password')
    server.sendmail('@gmail.com', to, content)
    server.close()
'''


# main program
print('Initializing Jarvis...')
speak('Initializing Jarvis...')
greet_master()
speak('I am Jarvis. How may I help you today?')

while True:
    # wait for user to speak and say Jarvis... xyz
    query = listen()
    if query != None:
        query = query.lower()
    if query != None and 'jarvis' in query:
        # when user asks Jarvis a question then run if checks
        if 'hello jarvis' in query:
            greet_master()
        elif 'google' in query:
            head, sep, tail = query.partition('google')
            speak(f'Searching Google for {tail}')
            open_url(f'google.com/search?q={tail}')
        elif 'youtube' in query:
            head, sep, tail = query.partition('youtube')
            speak(f'Searching YouTube for {tail}')
            open_url(f'youtube.com/results?search_query={tail}')
        elif 'open' in query:
            if '.com' in query:
                query_pieces = query.split(' ')
                for piece in query_pieces:
                    if '.com' in piece:
                        url = piece
                        print('found url ' + url)
                        open_url(url)
                        break
        elif 'spell' in query:
            word = query.split('spell')
            word = word[1][1:]
            characters = list(word)
            characters = ' '.join(characters)
            print(f'{word} is spelled {characters}')
            speak(f'{word} is spelled {characters}')
        elif "what time" in query:
            hour = int(datetime.now().hour)
            minutes = int(datetime.now().minute)

            if hour < 12:
                am_pm = 'AM'
            elif hour >= 12:
                am_pm = 'PM'

            if hour > 12:
                hour = hour - 12

            speak(f'It is currently {hour} {minutes} {am_pm}')
        elif 'volume' in query:
            if '%' in query:
                percent = int(re.search(r'\d+', query).group())
                speak(f'Changing volume to {percent}%.')
                volume.set_volume(volume.get_dB(percent))
                speak(f'Changed volume to {percent}%.')
            elif 'up' in query:
                speak('Increasing volume...')
                volume.up()
                speak('Volume has been increased!')
            elif 'down' in query:
                speak('Decreasing volume...')
                volume.down()
                speak('Volume has been decreased!')
            elif 'mute' in query:
                speak('Muting volume...')
                volume.mute()
                speak('Volume has been muted!')
            elif 'unmute' in query:
                speak('Unmuting volume...')
                volume.unmute()
                speak('Volume has been unmuted!')
        elif 'shut down' in query:
            speak(f'Shutting down... Good bye {MASTER}.')
            break