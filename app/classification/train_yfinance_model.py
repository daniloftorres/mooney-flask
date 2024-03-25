import yfinance as yf

# Definindo o ticker da ação e o intervalo de tempo
ticker = "AAPL"
inicio = "2020-01-01"
fim = "2021-01-01"

# Baixando os dados
dados = yf.download(ticker, start=inicio, end=fim)

# Visualizando os primeiros registros
print(dados.head())

# Divisão dos Dados
from sklearn.model_selection import train_test_split

X = dados.drop(['Adj Close'], axis=1)  # Usando como exemplo todas as colunas exceto 'Adj Close' como features
y = dados['Adj Close']  # Supondo que queremos prever o 'Adj Close'

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinamento do Modelo
from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Avaliação do Modelo
from sklearn.metrics import mean_squared_error

previsoes = modelo.predict(X_test)
mse = mean_squared_error(y_test, previsoes)
print(f"MSE: {mse}")
