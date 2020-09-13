
development:
	docker-compose build --force-rm --parallel
	docker-compose up -d
	docker-compose exec api python manage.py migrate
	docker-compose exec api python manage.py create_dynamo_tables

dynamo-tables:
	docker-compose up -d
	docker-compose exec api sh -c 'FLASK_APP=application flask shell'
