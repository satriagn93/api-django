# CRM-with-django

Create Modul mini CRM with django 2.1.7 dan python 3

Database = postgresql

1. install django 2.1.7 dan python 3

check django version: django-admin --version

check python version: python -V

2. install dan create virtualenv

3. clone project didalam folder environment 

   ketik di terminal " git clone https://github.com/satriagn93/CRM-with-django.git "

4. buat database dengan nama minicrmdjango

5. setting database didalam folder minicrm > settings.py pada bagian:

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

6. install requirements: pip install requirements.txt

7. migrate database: 

./manage.py makemigrations

./manage.py migrate

8. jalankan aplikasi: ./manage.py runserver
 