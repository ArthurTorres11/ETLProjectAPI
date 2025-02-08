# ETLProjectAPI

## Descrição
Este projeto é uma aplicação de ETL (Extract, Transform, Load) que utiliza a biblioteca `requests` para extrair dados de preços de criptomoedas da API do Coinbase, transformá-los e armazená-los em um banco de dados PostgreSQL hospedado no Render.

## Estrutura do Projeto
- `main.py`: Script principal que realiza o processo de ETL com integração ao PostgreSQL.

## Requisitos
- Python 3.8+
- Bibliotecas Python:
  - requests: Para fazer requisições HTTP à API do Coinbase.
  - sqlalchemy: Para mapeamento objeto-relacional (ORM) e interação com o banco de dados PostgreSQL.
  - psycopg2: Driver PostgreSQL para Python.
  - python-dotenv: Para carregar variáveis de ambiente de um arquivo `.env`.

## Instalação
Clone o repositório e instale os requisitos:
```sh
git clone https://github.com/seu-usuario/ETLProjectAPI.git
cd ETLProjectAPI
pip install -r requirements.txt

Configuração
Configure as variáveis de ambiente necessárias no arquivo .env:

POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=seu_banco_de_dados

Uso
Execute o script principal para iniciar o processo de ETL:

python main.py

Estrutura do Código
extrair_dados(): Função que faz a requisição à API do Coinbase e retorna os dados em formato de texto.
transformar_dados(dados): Função que transforma os dados extraídos, convertendo-os para o formato necessário.
load_dados_postgres(dados): Função que carrega os dados transformados no banco de dados PostgreSQL.
criar_tabela(): Função que cria a tabela no banco de dados PostgreSQL, se ela não existir.
Banco de Dados
O banco de dados utilizado é o PostgreSQL, hospedado no Render. A tabela bitcoin_preco é criada automaticamente pelo script, se não existir, e possui a seguinte estrutura:

CREATE TABLE bitcoin_preco (
    id SERIAL PRIMARY KEY,
    valor FLOAT NOT NULL,
    criptomoeda VARCHAR(10) NOT NULL,
    moeda VARCHAR(10) NOT NULL,
    timestamp TIMESTAMP WITHOUT TIME ZONE NOT NULL
);

API do Coinbase
A API do Coinbase é utilizada para obter os preços atuais das criptomoedas. A URL utilizada para a requisição é https://api.coinbase.com/v2/prices/spot. A resposta da API é um texto contendo informações sobre o preço da criptomoeda.

Bibliotecas Utilizadas
requests: Biblioteca para fazer requisições HTTP de forma simples e eficiente.
sqlalchemy: Biblioteca de ORM que facilita a interação com bancos de dados relacionais.
psycopg2: Driver PostgreSQL para Python, utilizado pelo SQLAlchemy para se conectar ao banco de dados.
python-dotenv: Biblioteca para carregar variáveis de ambiente a partir de um arquivo .env.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.