#!/bin/bash
cd /wwwroot
supervisorctl stop gunicorn
python3 manage.py runserver 0.0.0.0:8001
supervisorctl start gunicorn