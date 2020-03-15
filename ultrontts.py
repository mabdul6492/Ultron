import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        speak('Good Morning')
    elif (hour >= 12) and (hour < 18):
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak('Hello I am ultron. How may I help you')


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)  # here
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=10)

    try:
        print('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said : {query}\n')
    except Exception as e:
        print(e)
        print('Say that again please...')
        return 'None'
    return query


if __name__ == '__main__':
    wishme()
    take_command()
    take_command()

