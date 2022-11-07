from PySimpleGUI import PySimpleGUI as sg
from main import evaluate
import keyboard

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Assistente Virtual')],
    [sg.Input(key='texto')],
    [],
]
# Janela
janela = sg.Window('Vox Commands', layout)
# Ler Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if keyboard.is_pressed('p'):
        valores['texto'] = evaluate