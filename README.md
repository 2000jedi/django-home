# django-home
My Home Website. Note that you need to configure basic website detail under admin mode to correctly setup the server.

## Initial Configuration

> ./manage.py makemigrations
> ./manage.py migrate

You also need to create an admin account.

> ./manage.py createsuperuser

Then you can run the server in either debug or production mode.

## Run the server in debug mode

> ./manage.py runserver \<ip\>:\<port\>

## Requirements

- django
- django-markdownx
