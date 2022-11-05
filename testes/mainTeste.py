#!/usr/bin/env python3

import os
import pyttsx3
import core
from nlu.classifier import classify,max_seq

# SINTESE DE FALA
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def evaluate(text):
    entity = classify(text)
    if entity == 'time\getTime':
        speak(core.SystemInfo.get_time())
        return ""
    elif entity == 'time\getDate':
        speak(core.SystemInfo.get_date())
    # Abrir programas
    elif entity == 'open\\notepad':
        speak('Abrindo o bloco de notas')
        os.system('notepad.exe')
    elif entity == 'open\\word':
        speak('Abrindo o word')
        os.system('"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"')
    elif entity == 'open\\chrome':
        speak('Abrindo o chrome')
        os.system('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
    elif entity == 'open\\wMP':
        speak('Abrindo o reprodutor de mídia')
        os.system('"C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe"')

    print('Text: {} Entity: {}' .format(text, entity))
    return text

while True:
    text = input('O que você quer dizer ao Assistente Virtual?\n')
    if len(text) > max_seq:
        text = ""
    elif len(text) < max_seq:
        evaluate(text)