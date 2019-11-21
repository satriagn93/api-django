Django REST framework is a powerful and flexible toolkit for building Web APIs.

Requirements:
REST framework requires the following:

Python (3.5, 3.6, 3.7)
Django (1.11, 2.0, 2.1, 2.2)

Installation:
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

Add 'rest_framework' to your INSTALLED_APPS setting.

INSTALLED_APPS = [
    ...
    'rest_framework',
]

1. install dan create virtualenv

2. clone project didalam folder environment 

3. buat database dengan nama minicrmdjango

4. setting database didalam folder minicrm > settings.py pada bagian:

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'minicrmdjango',

        'USER': 'postgres',

        'PASSWORD': 'password',

        'HOST': 'localhost',

        'PORT': '',
    }

}

5. install requirements: pip install requirements.txt

6. migrate database: 

    6.1 ./manage.py makemigrations

    6.2 ./manage.py migrate

7. jalankan aplikasi: ./manage.py runserver
 