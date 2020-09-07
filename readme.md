# J.A.R.V.I.S.

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


# config.py
```
MASTER = 'Austin'

# text to speech
tts_voice_rate = 145
```


# To Do
- [ ] research how to setup and use recognize_sphinx(): CMU Sphinx this allows local speech recognition instead of relying on an internet connection
- [ ] figure out how to change volume on mac/linux
- [ ] test all commands on mac/linux
- [x] add command jarvis google xyz
- [x] add command jarvis youtube xyz
- [ ] add the ability to automatically login to websites. This will use Selenium and the auto install libraries for chrome/firefox drivers. Will need to create a class or set of functions that will allow me to setup multiple different logins with out hard coding each one. For example it would take input that tells the funtion where the xpath for the login form, username/email field, password field, submit button, etc is located. This configuration should all be in the config.py file.
- [ ] add ability to search wolframalpha
- [ ] add an ability to do a general search where jarvis will find a result from either, wolframalpha, wikipedia, or google to answer your question.
- [x] jarvis how do you spell "xyz" > output "you spell xyz like: x y z"
- [ ] create a ui/visual that responds to voice input and that reacts to jarvis speaking. kind of like a spectrum analyzer
