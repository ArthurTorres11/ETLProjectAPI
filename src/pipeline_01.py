import requests
from tinydb import TinyDB
from datetime import datetime
import time

def extrair_dados():
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    dados = response.json()
    return dados

def transformar_dados(dados):    
    valor = dados["data"]["amount"]
    criptomoeda = dados["data"]["base"]
    moeda = dados["data"]["currency"]
    timestamp = datetime.now().timestamp()

    dados_transformados = {
        "valor" : valor,
        "criptomoeda" : criptomoeda,
        "moeda" : moeda,
        "timestamp" : timestamp
    }
    
    return dados_transformados

def load_dados(dados, db_name="bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(dados)
    print("Dados salvos!")


if __name__ == "__main__":
    while True:
        dados_json = extrair_dados()
        dados_tratados = transformar_dados(dados_json)
        load_dados(dados_tratados)
        time.sleep(15)