Projeto de um sistema integrado com a API do twitter, utilizando Docker, Apache HOP e MongoDB. Também foi preparado um Jupyter Notebook utilizando a API do twitter para receber os trends. 

O projeto utiliza o poetry, então fica mais fácil identificar e instalar as dependências do projeto. Além disso roda através do docker compose, que indica as imagens a serem utilizadas nos containers.

O que falta? Não consegui fazer a conexão do mongodb dentro do docker com a venv do poetry. Resumindo, o arquivo arquivo mongo.py, que seria responsável por testar a conexão básica com o banco e fazer um insert simples, nao funcionou. Sendo assim, o código não foi mais desenvolvido nessa parte, devido ao curto prazo para entrega.

O projeto pode ser utilizado para iniciar o docker, com o mongodb e o mongodb express e o fastAPI.

Desafio DIO + Banco Carrefour
