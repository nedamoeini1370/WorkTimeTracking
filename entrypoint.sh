#!/bin/bash
python3 manage.py check
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn -b :8000 -w 2 --enable-stdio-inheritance --error-logfile '-' --access-logfile '-' --capture-output --log-level info WorkTimeTracker.wsgi