# flask_server_template
Flask Server Template ready to plug in business logic.

Features of this template are:
1. Flask configuration module
2. Application configuration module
3. Server logging
4. Connection to DB using
  a. SQLAlchemy Core: This allows you write raw sql statements
  b. SQLAlchemy ORM: Pythonic way to interact with database using object relationship mapping and reflecting existing tables into python objects
5. Database query results in pandas dataframe objects for easy processing

More features can be added on suggestion.

In general, it should easy to deploy and get you running.

The deployment steps are>

$mkdir base

$cd base

$git clone https://github.com/alsm6169/flask_server_template.git

$cd flask_server_template/

$conda create --name ptest

$conda activate ptest

$conda install --file requirements.txt

$python main.py
