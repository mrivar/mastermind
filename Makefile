all: libs migrations run

run_with_migrations: migrations run

libs:
	@echo "Installing libraries..."
	pip install --progress-bar on --no-cache-dir -r requirements.txt

style:
	@echo "Analysing coding style..."
	pylint-fail-under --ignore=migrations --django-settings-module=mastermind.settings --fail_under 8.00 mastermind game guess

test:
	@echo "Performing Unit & Integration tests..."
	python manage.py test

coverage:
	@echo "Calculating coverage..."
	coverage run --source='.' manage.py test

docker:
	@echo "Building Docker image..."
	docker build . -t mastermind

migrations:
	@echo "Applying database migrations..."
	python manage.py makemigrations
	python manage.py migrate

remove_database:
	@echo "Removing local database..."
	rm db.sqlite3
	rm -r */migrations/*

collectstatic:
	@echo "Collecting static files..."
	python manage.py collectstatic

run:
	@echo "Running application locally..."
	python manage.py runserver

run_gunicorn:
	@echo "Running gunicorn server..."
	(gunicorn mastermind.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) & nginx -g "daemon off;"
