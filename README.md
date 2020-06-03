<h1>Controle de gasto Python Django</h1>

<h2>Projeto controle de gastos com Python e Django.</h2>

![file](https://i.imgur.com/SBW6YlN.png "file")

<h3>Pastas criadas no desenvolvimento do projeto. </h3>
Venv - Virtualenv com Django instalado e db.sqlite3 

	python -m venv venv

<h3>Dentro da vm é instalado o Django com o comando:</h3>

	pip install django 

<h3>Contas - App</h3>

	python manage.py startapp contas

<h3>Controle_gastos - projeto Django, para cria-lo , devemos digitar: </h3>

	django-admin startproject controle_gastos


<h3>db.sqlite3 - O django vem com o banco de dados SQLite 3, quando intalado ele carrega várias tabélas para serem utilizadas.</h3>

	python manage.py migrate


Para acessar a aplicação após uma modificação no banco de dodos utiliza o
comando migrations
python manage.py migrate e makemigrations 
	
makemigrations - responsável por criar novas migrações.

migrations - aplica as migrações.

Documentação - migrations no Django 

[Migrations - Django documentation ](http://https://docs.djangoproject.com/en/3.0/topics/migrations/ "Migrations - Django documentation ")


![makemigrations e migrate](https://i.imgur.com/2791IEf.png "makemigrations e migrate")
	
	python manage.py makemigrations
	python manage.py migrate
	manage.py runserver  - > Inicia o server 
