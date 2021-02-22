import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes




listener =sr.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice =listener.listen(source)
            commmand = listener.recognize_google(voice)
            commmand = commmand.lower()
            if 'alexa' in commmand:
                commmand = commmand.replace('alexa','')
                print(commmand)

    except:
        pass
    return commmand
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry iam ill')
    elif 'are you single' in command:
        talk('no iam in relation with my company')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the it angain')

while True:
    run_alexa()
