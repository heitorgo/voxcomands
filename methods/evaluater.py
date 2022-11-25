from nlu.classifier import classify, max_seq
from methods.speaker import speak
import webbrowser as wb
import core
import os

def evaluate(text):
    if len(text) < max_seq:
        entity = classify(text)
        if entity == 'time\getTime':
            speak(core.SystemInfo.get_time())
            return ""
        elif entity == 'time\getDate':
            speak(core.SystemInfo.get_date())
        # Abrir programas
        # Bloco de notas
        elif entity == 'open\\notepad':
            speak('Abrindo o bloco de notas')
            os.system('notepad.exe')
        # Word
        elif entity == 'open\\word':
            speak('Abrindo o word')
            os.system('"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"')
        # Windows Media Player
        elif entity == 'open\\wMP':
            speak('Abrindo o reprodutor de mídia')
            os.system('"C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe"')
        # Dosvox
        elif entity == 'open\\dosvox':
            speak('Abrindo o Dosvox')
            os.system('"C:\\Winvox\\dosvox.exe"')
        # Jaws
        elif entity == 'open\\jaws':
            speak('Abrindo o Jaws')
            os.system('"C:\\Program Files\\Freedom Scientific\\JAWS\\2022\\jfw.exe"')
        # Acessando sites
        # Google
        elif entity == 'access\\google':
            speak('Acessando o google')
            wb.open('https://www.google.com.br/')
        # Gmail
        elif entity == 'access\\gmail':
            speak('Acessando o gmail')
            wb.open('https://www.google.com/intl/pt/gmail/about/')
        # Dosvox
        elif entity == 'access\\dosvox':
            speak('Acessando o dosvox')
            wb.open('http://intervox.nce.ufrj.br/dosvox/')
        # Google tradutor
        elif entity == 'access\\gglTranslate':
            speak('Acessando o google tradutor')
            wb.open('https://translate.google.com.br/?hl=pt-BR')
        # Jaws
        elif entity == 'access\\jaws':
            speak('Acessando o Jaws')
            wb.open('https://www.freedomscientific.com/products/software/jaws/')
        # Mecdaisy
        elif entity == 'access\\mecdaisy':
            speak('Acessando o mecdaisy')
            wb.open('http://intervox.nce.ufrj.br/mecdaisy/')
        # Virtual Vision
        elif entity == 'access\\virtualvision':
            speak('Acessando o site virtual vision')
            wb.open('https://www.virtualvision.com.br/')
        # NVDA
        elif entity == 'access\\nvda':
            speak('Acessando o NVDA')
            wb.open('https://www.nvaccess.org/')
    else:
        entity = 'text\\tooBig'
    
    print('Text: {} Entity: {}' .format(text, entity))
    return entity
