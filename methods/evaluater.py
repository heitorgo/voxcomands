from nlu.classifier import classify
from methods.speaker import speak
import webbrowser as wb
import core
import os

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
    elif entity == 'open\\wMP':
        speak('Abrindo o reprodutor de mídia')
        os.system('"C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe"')
    elif entity == 'open\\dosvox':
        speak('Abrindo o Dosvox')
        os.system('"C:\\Winvox\\dosvox.exe"')
    elif entity == 'open\\jaws':
        speak('Abrindo o Jaws')
        os.system('"C:\\Program Files\\Freedom Scientific\\JAWS\\2022\\jfw.exe"')
    elif entity == 'open\\mecdaisy':
        speak('Abrindo o Mecdaisy')
        os.system('"C:\\Program Files (x86)\\NCEMEC\\MecDaisy\\MecDaisy.jar"')
    # Acessando sites
    elif entity == 'access\\google':
        speak('Acessando o google')
        wb.open('https://www.google.com.br/')
    elif entity == 'access\\gmail':
        speak('Acessando o site do gmail')
        wb.open('https://www.google.com/intl/pt/gmail/about/')
    elif entity == 'access\\dosvox':
        speak('Acessando o site do dosvox')
        wb.open('http://intervox.nce.ufrj.br/dosvox/')
    elif entity == 'access\\gglTranslate':
        speak('Acessando o site do google tradutor')
        wb.open('https://translate.google.com.br/?hl=pt-BR')
    elif entity == 'access\\jaws':
        speak('Acessando o Jaws')
        wb.open('https://www.freedomscientific.com/products/software/jaws/')
    elif entity == 'access\\mecdaisy':
        speak('Acessando o site do mecdaisy')
        wb.open('http://intervox.nce.ufrj.br/mecdaisy/')
    
    print('Text: {} Entity: {}' .format(text, entity))
