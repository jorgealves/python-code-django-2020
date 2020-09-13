
development:
	docker-compose build --force-rm --parallel
	docker-compose up -d  --remove-orphans
	docker-compose exec api python manage.py migrate
	docker-compose exec api python manage.py create_dynamo_tables
