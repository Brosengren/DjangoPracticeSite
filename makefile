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

venv:
	source ./.venv/bin/activate

admin-user:
	python manage.py createsuperuser