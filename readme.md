# J.A.R.V.I.S.


# Building apk from Windows 10
- Setup Windows Subsystem for Linux https://docs.microsoft.com/en-us/windows/wsl/install-win10
- ~~Install the Remote - WSL plugin for vscode~~
- Now open WSL
- Navigate to the folder with your code example: `cd /mnt/c/users/austin/desktop/non_web_apps/jarvis`
- Create a virtual enivronment using `python3 venv venvWSL`
- Activate venv `source venvWSL/bin/activate`
- Run these commands (copied from https://buildozer.readthedocs.io/en/latest/installation.html#targeting-android):
```
pip3 install --upgrade buildozer
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip3 install --user --upgrade Cython==0.29.19 virtualenv  # the --user should be removed if you do this in a venv

# add the following line at the end of your ~/.bashrc file
export PATH=$PATH:~/.local/bin/
```
- `buildozer init`
- `buildozer -v android debug`
- to send and run on your android device `buildozer android debug deploy run`

# Available voice commands
You need to include jarvis in every command so jarvis knows you want it to do something.

- hello jarvis > says hello back
- open 'yourwebsite'.com > opens whatever .com website you tell it
- google 'xyz' > opens google and searchs 'xyz'
- youtube 'xyz' > opens youtube and searchs 'xyz'
- what time > tells you the time
- volume x% > changes volume to x%
- volume up > increases volume by 5 dB
- volume down > decreases volume by 5 dB
- volume mute > mutes volume
- volume unmute > unmutes volume
- shut down > shuts down jarvis
- spell "xyz" > "xyz is spelled x y z"
- wolframalpha "weather"> returns the current weather or whatever you ask.
- search "xyz" OR what is "xyz" > will speak the search result if found by Wolfram Alpha or Wikipedia. If not found will open Google.
- login to "github" > uses selenium to log you into github or any website you specify as log as it is in the config.py file.
- start timer X hours X minutes X seconds > starts a timer for specified time
- time left on timer > gives you the amount of time left on your timer
- stop timer > stops your current timer


# config.py
```
MASTER = 'Austin'
JARVIS = 'python'

# text to speech
tts_voice_rate = 145

# wolframalpha
WOLF_APPID = 'YourAppID'

# this allows you to specify a login and selenium commands to automatically log you into a website
# since it is a list you can have multiple different logins setup at once!
login = [
    {
        'website': 'https://github.com/login',
        'username': '',
        'password': '',
        'selenium_commands': [
            {
                'type': 'input',
                'xpath': '//*[@id="login_field"]',
                'input_variable': 'username'
            },
            {
                'type': 'input',
                'xpath': '//*[@id="password"]',
                'input_variable': 'password'
            },
            {
                'type': 'button',
                'xpath': '//*[@id="login"]/form/div[4]/input[9]'
            }
        ]
    }
]
```


# To Do
- [ ] research how to setup and use recognize_sphinx(): CMU Sphinx this allows local speech recognition instead of relying on an internet connection
- [ ] figure out how to change volume on mac/linux
- [ ] test all commands on mac/linux
- [x] add command jarvis google xyz
- [x] add command jarvis youtube xyz
- [x] add the ability to automatically login to websites. This will use Selenium and the auto install libraries for chrome/firefox drivers. Will need to create a class or set of functions that will allow me to setup multiple different logins with out hard coding each one. For example it would take input that tells the funtion where the xpath for the login form, username/email field, password field, submit button, etc is located. This configuration should all be in the config.py file.
- [x] add ability to search wolframalpha
- [x] add an ability to do a general search where jarvis will find a result from either, wolframalpha, wikipedia, or google to answer your question.
- [x] jarvis how do you spell "xyz" > output "you spell xyz like: x y z"
- [ ] add ability to send emails
- [ ] add ability to send text messages. this would use the text via email functionality. like sending an email to 1234567890@tmobile.com will send a text message to the phone number.
- [ ] play "song name" using spotify api spotipy
- [ ] create a to do list. Jarvis can run CRUD operations against the to do list.
- [ ] ability to have multiple to do lists.
- [x] countdown timer
- [ ] alarm clock
- [ ] check grammar of copied text?
- [ ] turn into a kivy application so Jarvis can be mobile!
- [ ] create a ui/visual that responds to voice input and that reacts to jarvis speaking. kind of like a spectrum analyzer
- [ ] figure out how to monetize the kivy mobile application. text ads, video ads, audio ads???
- [ ] analytics for mobile app???
- [ ] create automated tests that will test all the commands?
- [ ] create new rows in xls files with jarvis. use pandas or openpyxl? commands: open spreadsheet, close spreadsheet, add row to file
- [ ] Hook up google calanader and hav Jarvis tell teh user when they have their next meeting, or the next thing on their schedule 5/10 minutes before it starts. Time Jarvis says it at can be a variable in config.py
- [ ] Ability to ask Jarvis how much battery percentage is left on your device (phone, laptop, etc)
