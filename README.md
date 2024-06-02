# datafun-05-sql
This folder contain material for our 5th project over sql
# datafun-05-sql
## Create Project Virtual Environment and update pip and install requests

On mac, create a project virtual environment in the .venv folder. 

''' zsh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pandas pyarrow
python3 -m pip freeze > requirements.txt
mkdir .gitignore
'''
## add lines .venv/ and .vscode/ to .gitignore file

## Git add and commit

'''zsh
git add .
git commit -m "add .gitignore, cmds to readme"
git push origin main
'''

## Create db_initialize_charlietodd.py file to obtain the data for the tables used in the SQL files inside the project folder. 

## Create db_operations_charlietodd.py which creates tables and inserts records from the sql folder. I also created it to create a log.txt file. A few bugs were worked out and now the .py file creates tables and populates data into them from csv files

## I created a variety of sql files that interact with db_operations_charlietodd.py file to do a variety of operations within my database. 

## Specification
'''
This project was built to the following specification:

- [datafun-05-spec](https://github.com/denisecase/datafun-05-spec)
'''
