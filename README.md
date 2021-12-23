--Backend ECommerce with DJango REST Framework--

Steps to deploy the backend:

1- Install Python 3.10.1 or newer. (https://www.python.org/downloads/)

2- You decide which database to use. Consult the official documentation for supported databases.  
    If you are using MySQL, install Xampp (https://www.apachefriends.org/es/download.html).
    Then, from the xampp control panel, launch apache and mysql
    
        Consult https://docs.djangoproject.com/en/4.0/ref/databases/

3- Download or clone the project to a folder named server

4- Create a virtual environment for the project:

        Windows : python -m venv enviroment_name
        Linux : python3 -m venv enviroment_name

5- Activate the virtual environment:

        Windows : enviroment_name/Scripts/activate.ps1
        Linux : source enviroment_name/bin/activate

        Consult https://docs.python.org/es/3/tutorial/venv.html

6- Install project dependencies:

        pip install -r requirements.txt

7- Configure the environment variables in an .env file. Pay special attention to the variables in the configurations.
    (settings/base.py, settings/local.py and settings/production.py)

8- If I use the configuration with MySQL create the database, with the name I specify in the environment variabe DATABASE_NAME

    To configure other databases, refer to the documentation. https://docs.djangoproject.com/en/4.0/ref/databases/

9- Run project migrations:

        Windows: python manage.py migrate
        Linux: python3 manage.py migrate

!- Before starting the server, verify that settings are applied in the wsgi.py, asgi.py, and manage.py files:
    server.settings.production or server.settings.local
    The main difference is the state of the DEBUG constant. -!

10- Create a super user:

        Windows: python manage.py createsuperuser
        Linux: python3 manage.py createsuperuser

11- Start the server:

        Windows: python manage.py runserver
        Linux: python3 manage.py runserver
