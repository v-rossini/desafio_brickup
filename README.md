# desafio_brickup

O projeto foi criado usando o Poetry para realizar o gerenciamento de dependencias.

## Para instalar o poetry:
* pip install poetry

## para definir o diretório do projeto como padrão para a pasta .env para :
* poetry config virtualenvs.in-project true

## Para criar o ambiente virtual e instalar dependências:
* poetry install

## para iniciar o ambiente virtual e abrir o shell:
* poetry shell

## para rodar o projeto:
* cd ./app
* uvicorn main:app --reload

--------------------------
o projeto irá rodar na porta localhost:8000 (documentação da API em localhost:8000/docs)
