from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import pickle

colunas = ['tamanho', 'ano', 'garagem']
modelo = pickle.load(open('../../models/modelo.sav', 'rb'))


app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'lucas'
app.config['BASIC_AUTH_PASSWORD'] = 'guts'

basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return 'Olá, mundo!'


@app.route('/sentimento/<frase>')
@basic_auth.required
def sentimento(frase):
    #translator = Translator()
    tb = TextBlob(frase)
    #tb_en = tb.translate(from_lang='pt_br', to='en')
    polaridade = tb.sentiment.polarity
    return f'Polaridade: {polaridade}'

@app.route('/cotacao/',methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])
    return jsonify(preco = preco[0])

app.run(debug=True, host='0.0.0.0')

#Para gerar o ambiente virtual: python -m virtualenv venv
#Para ativar o ambiente virtual: venv\Sripts\activate
#Para entrar na pasta do projeto: cd mlops-deploy\src\app