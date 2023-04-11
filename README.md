# duguncomapi
Very simple Django API for adding, deleting, updating, listing product information

düğün.com Simple API project
Steps that I followed:

Environment setup
- Created a project folder on my local disk (apiproject)
- Created a virtual environment inside that folder (python -m venv {name of your virtual environment})
- Installed the following frameworks inside my venv:
    * Django
    * Django REST framework


Creating our application

(While inside apiproject folder) django-admin startproject duguncomapi
Go to settings.py, and add ‘rest_framework’ in the “INSTALLED_APPS” section. 

Initial migration
(While in duguncomapi in terminal) run “python3 manage.py migrate”


Done. Our local server is up and running :) 
