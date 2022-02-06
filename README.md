# **WorkTime Tracker service**

A multi-user and multi-project work time tracking application using Django and Django Rest Framework.

Users can add some tasks under every project, and the time that users have spent on the task (suspend time and total time) is calculated(track work time).

### **Tech stack**
This service is written in python and Django Rest Framework to serve REST API.

Python 3.9

Django 4.0.1

Django Rest Framework

Django openapi swagger

Docker

Docker Compose

### **How to use Service:**

**1. build the service locally**

`$ virtualenv venv`

`$ . venv/bin/activate`

`$ pip install -r requirements.txt`

`$ python manage.py makemigrations`

`$ python manage.py migrate`

`$ python manage.py collectstatic --noinput`

`$ python manage.py runserver 8000`

**2- build the service in local docker**

based on python:3.9 image

`make build_gunicorn`

`docker-compose up`

### **Swagger API documentation**

navigate to /swagger in browser to use swagger

### **Automatic tests**

`python manage.py test`

### **Future Improvements**
Improve Test coverage.

Improve Tracker business. 