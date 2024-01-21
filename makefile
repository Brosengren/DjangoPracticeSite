SHELL = /bin/sh

run:
	python manage.py runserver

run-full:
	python manage.py runserver 0.0.0.0:8000

shell:
	python manage.py shell

setup: 
	pip install -r requirements.txt

clean:
	rm -rf __pycache__

admin-user:
	python manage.py createsuperuser

ready-deploy:
	python manage.py collectstatic
	python manage.py makemigrations
	python manage.py migrate