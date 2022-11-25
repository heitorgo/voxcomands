from methods.evaluater import evaluate
from nlu.classifier import max_seq

while True:
    text = input('O que você quer dizer ao Assistente Virtual?\n')
    if len(text) > max_seq:
        text = ""
    elif len(text) < max_seq:
        evaluate(text)