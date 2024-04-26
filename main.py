from flask import Flask
from textblob import TextBlob
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

url = 'https://raw.githubusercontent.com/alura-cursos/1576-mlops-machine-learning/aula-5/casas.csv'
df = pd.read_csv(url)
colunas = ['tamanho', 'preco']
df = df[colunas]
df.head()
x = df.drop('preco', axis = 1)
y = df['preco']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=42)
modelo = LinearRegression()
modelo.fit(x_train, y_train)

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

@app.route('/cotacao/<int:tamanho>')
def cotacao(tamanho):
    preco = modelo.predict([[tamanho]])
    return f'Preço estimado: R$ {preco[0]:.2f}'

app.run(debug=True)