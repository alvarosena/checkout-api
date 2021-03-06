# Checkout API with Python Flask

## Setup & Instalation
Make sure you have the lastest version of Python.
<pre>git clone 'repository'</pre>

### Active the environment and running the app
Activate the environment Linux and MacOS:
<pre>. envm/bin/activate</pre>
Install all project dependecies
<pre>pip3 install -r requirements.txt</pre>
Run the app
<pre>flask run</pre>

## Technologies
 - Python
 - Flask
 - SQLAlchemy
 - Flask-Migrate
 - SQLite

## API Reference

__POST CREATE BUYER__
```json
{
    "name": "Brian Craw",
    "email": "brian@example.com",
	"cpf": "00000000000"
}
```
__Response status code 201__
```json
{
    "id": 1,
    "name": "Brian Craw",
    "email": "brian@example.com",
    "cpf": "00000000000"
}
```

__Response status code 400__
```json
{
    "error": "Buyer already exists"
}
```