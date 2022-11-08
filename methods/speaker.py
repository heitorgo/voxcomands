import pyttsx3


# SINTESE DE FALA
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
