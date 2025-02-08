# ETLProjectAPI

## Descrição
Este projeto é uma aplicação de ETL (Extract, Transform, Load) que utiliza a biblioteca `requests` para extrair dados de uma API, transformá-los conforme necessário e carregá-los em um banco de dados.

## Estrutura do Projeto
- `extract.py`: Contém funções para extrair dados da API.
- `transform.py`: Contém funções para transformar os dados extraídos.
- `load.py`: Contém funções para carregar os dados transformados no banco de dados.
- `main.py`: Script principal que orquestra o processo de ETL.

## Requisitos
- Python 3.8+
- Bibliotecas Python:
  - requests
  - pandas
  - sqlalchemy

## Instalação
Clone o repositório e instale os requisitos:
```sh
git clone https://github.com/seu-usuario/ETLProjectAPI.git
cd ETLProjectAPI
pip install -r requirements.txt