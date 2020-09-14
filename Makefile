
development:
	docker-compose build --force-rm --parallel
	docker-compose up -d  --remove-orphans
	sleep 5
	docker-compose exec api python manage.py migrate
	docker-compose exec api python manage.py refresh_dynamodb_tables
	docker-compose exec api python manage.py import_data_from_omdb

