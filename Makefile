all: libs migrations run

run_with_migrations: migrations run

libs:
	@echo "Installing libraries..."
	pip install --progress-bar emoji --no-cache-dir -r requirements.txt

test:
	@echo "Performing Unit & Integration tests..."
	python manage.py test

coverage:
	@echo "Calculating coverage..."
	coverage run --source='.' manage.py test

docker:
	@echo "Building Docker image..."
	@echo "not implemented yet"

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
	@echo "Running application..."
	python manage.py runserver
