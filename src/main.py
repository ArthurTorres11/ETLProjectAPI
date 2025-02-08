import requests
from datetime import datetime
import time
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, BitcoinPreco

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def criar_tabela():
    Base.metadata.create_all(engine)
    print("Tabela criada!")

def extrair_dados():
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    dados = response.json()
    return dados

def transformar_dados(dados):    
    valor = dados["data"]["amount"]
    criptomoeda = dados["data"]["base"]
    moeda = dados["data"]["currency"]
    timestamp = datetime.now()  # Converte para datetime

    dados_transformados = {
        "valor" : valor,
        "criptomoeda" : criptomoeda,
        "moeda" : moeda,
        "timestamp" : timestamp
    }
    
    return dados_transformados

def load_dados_postgres(dados):
    session = Session()
    novo_registro = BitcoinPreco(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    print(f"[{dados['timestamp']}] Dados salvos no PostgreSQL!")

if __name__ == "__main__": 
    criar_tabela()
    print("Iniciando pipeline ETL com atualização a cada 15 segundos... (CTRL+C para interromper)")

    while True:
        try:
            dados_json = extrair_dados()
            if dados_json:
                dados_tratados = transformar_dados(dados_json)
                print("Dados Tratados:", dados_tratados)
                load_dados_postgres(dados_tratados)
        except KeyboardInterrupt:
            print("Processo interrompido pelo usuário. Finalizando...")
            break
        except Exception as e:
            print(f"Erro inesperado durante a pipeline: {e}")
        time.sleep(15)