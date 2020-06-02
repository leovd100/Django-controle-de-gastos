##Controle de gasto Python Django

Projeto controle de gastos com Python e Django.

![file](https://i.imgur.com/SBW6YlN.png "file")

Pastas criadas no desenvolvimento do projeto. 
Venv - Virtualenv com Django instalado e db.sqlite3 

	python -m venv venv

Dentro da vm é instalado o Django com o comando:

	pip install django 

Contas - App

	python manage.py startapp contas

Controle_gastos - projeto Django, para cria-lo , devemos digitar: 

	django-admin startproject controle_gastos


db.sqlite3 - O django vem com o banco de dados SQLite 3, quando intalado ele carrega várias tabélas para serem utilizadas.

	python manage.py migrate


