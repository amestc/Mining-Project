Este projeto foi feito e idealizado para o trabalho da faculdade UniFecaf para a ExpoTech

-------------------------------------------

Trabalho feito por:
--------------------------------------------------------------------------------------

Camila Cesco Ferreira

Isabella Santos de Albuquerque Zanin

Leandro Laurindo Soares

Marcelo Luna Ierardi

Pedro Henrique Pedroso

--------------------------------------------------------------------------------------

Para que este projeto funcione corretamente deve se seguir os seguintes passos:
-------------------------------------------

--------------------------------------------------------------------------------------
Instalar:
-------------------------------------------
Python 3.10 ou superior

Banco de dados: de preferencia MySql Workbench

-------------------------------------------

Instalar as seguintes extensões do VsCode:
-------------------------------------------
Live server

Python

-------------------------------------------

Rodar no terminal:
-------------------------------------------

pip install sqlalchemy

pip install pymysql

pip install cryptography

pip install flask

pip install flask-cors

python -m pip install requests geopy

-------------------------------------------

Criar o banco mineradora no banco de dados
-------------------------------------------

create database mineradora;

-------------------------------------------

Editar no dbmining.py na linha 5 a rota para o banco de dados da seguinte forma
-------------------------------------------

db = create_engine("mysql+pymysql://[usuario do banco de dados]:[senha do usuario]@127.0.0.1:3306/mineradora")

-------------------------------------------

abrir e executar api.py

abrir o index.html e clicar em "Go Live" no canto inferior direito

-------------------------------------------
