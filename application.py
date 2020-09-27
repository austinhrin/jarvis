### preinstalled python dependancies
from datetime import datetime
import re
#import smtplib # will allow you to send emails

### pip installed dependancies
import pyttsx3
import speech_recognition as sr

### user created dependancies
from config import MASTER, JARVIS,tts_voice_rate
from modules.open import open_url, auto_login
from modules import volume, search, helpers, time


# text to speech
tts = pyttsx3.init('sapi5')
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[0].id)
tts.setProperty('rate',tts_voice_rate)

JARVIS = JARVIS.lower()

timer_time = 0
timer_duration = 0

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

def main_loop():
    global timer_duration
    global timer_time
    timer_duration = timer_duration
    timer_time = timer_time
    # wait for user to speak and say Jarvis... xyz
    query = listen()
    if query != None:
        # convert what is said to lowercase
        # to make life with if statements easier
        query = query.lower()
    if query != None and JARVIS in query:
        # when user asks Jarvis a question then run if checks
        if f'hello {JARVIS}' in query:
            greet_master()
        elif 'search' in query or 'what is' in query:
            # remove name of command and get search term
            try:
                search_term = helpers.string_after(query, 'search')
            except:
                search_term = helpers.string_after(query, 'what is')
            # try search wolframalpha
            wolf_response = search.wolf(search_term)
            if 'could not find' in wolf_response:
                # then wikipedia
                wiki_response = search.wiki(search_term)
                if 'could not find' in wiki_response:
                    # else search google
                    speak(f'Could not find {search_term} on Wolfram Alpha or Wikipedia opening Google.')
                    open_url(f'google.com/search?q={search_term}')
                else:
                    print(wiki_response)
                    speak(wiki_response)
            else:
                print(wolf_response)
                speak(wolf_response)
        elif 'loginto' in helpers.remove_spaces(query):
            # remove name of command and get search term
            if 'login to' in query:
                search_term = helpers.string_after(query, 'login to')
            elif 'log into' in query:
                search_term = helpers.string_after(query, 'log into')
            # open and login to the website
            login = auto_login(search_term)
            if login == True:
                speak(f'Logged into {search_term}')
            else:
                speak(f'Was not able to login to {search_term}')
        elif 'google' in query and 'open' not in query:
            # remove name of command and get search term
            search_term = helpers.string_after(query, 'google')
            speak(f'Searching Google for {search_term}')
            open_url(f'google.com/search?q={search_term}')
        elif 'youtube' in query and 'open' not in query:
            # remove name of command and get search term
            search_term = helpers.string_after(query, 'youtube')
            speak(f'Searching YouTube for {search_term}')
            open_url(f'youtube.com/results?search_query={search_term}')
        elif 'wolframalpha' in helpers.remove_spaces(query) and 'open' not in query:
            # remove name of command and get search term
            if 'wolfram alpha' in query:
                search_term = helpers.string_after(query, 'wolfram alpha')
            elif 'wolframalpha' in query:
                search_term = helpers.string_after(query, 'wolframalpha')
            # search wolframalpha
            response = search.wolf(search_term)
            print(response)
            speak(response)
        elif 'wikipedia' in query and 'open' not in query:
            # remove name of command and get search term
            search_term = helpers.string_after(query, 'wikipedia')
            response = search.wiki(search_term)
            print(response)
            speak(response)
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
        elif 'start timer for' in query:
            if timer_duration != 0:
                speak(f'There is already a timer. If you want to cancel the current timer say "stop timer".')
            else:
                timer_time = datetime.now()
                string_with_time = helpers.string_after(query, 'start timer for')
                # set the timer
                timer_duration = time.get_time_from_string(string_with_time)
                hour, minutes, seconds = timer_duration.split(':')
                speak(f'Timer started for {hour} hours {minutes} minutes and {seconds} seconds')
        elif 'time left on timer' in query:
            time_left = time.check_time_elapsed(timer_time, timer_duration)
            hour, minutes, seconds = time_left.split(':')
            speak(f'Your timer has {hour} hours {minutes} minutes and {seconds} seconds left.')
        elif 'stop timer' in query:
            speak(f'Timer stopped!')
            timer_time = 0
            timer_duration = 0
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
        elif 'shutdown' in helpers.remove_spaces(query):
            speak(f'Shutting down... Good bye {MASTER}.')
            #break
            return 'break'
    # check if there is a timer
    if timer_duration != 0:
        done = time.check_time_elapsed(timer_time, timer_duration)
        #print(done)
        if done == True:
            hour, minutes, seconds = timer_duration.split(':')
            speak(f'Your timer for {hour} hours {minutes} minutes and {seconds} seconds is up!')
            timer_time = 0
            timer_duration = 0

if __name__ == '__main__':
    print(f'Initializing {JARVIS}...')
    speak(f'Initializing {JARVIS}...')
    greet_master()
    speak(f'I am {JARVIS}. How may I help you today?')
    while True:
        a = main_loop()
        if a == 'break':
            break