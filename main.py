from flask import Flask

app = Flask('meu_app')

@app.route('/')
def home():
    return 'Olá, mundo!'
