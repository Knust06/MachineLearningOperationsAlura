from flask import Flask
from textblob import TextBlob
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, mundo!'


@app.route('/sentimento/<frase>')
def sentimento(frase):
    translator = Translator()
    tb = TextBlob(frase)
    #tb_en = tb.translate(from_lang='pt_br', to='en')
    polaridade = tb.sentiment.polarity
    return f'Polaridade: {polaridade}'

app.run(debug=True)