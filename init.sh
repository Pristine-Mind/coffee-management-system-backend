#! /bin/bash -xe

docker-compose exec web python manage.py loaddata load_coffee.json
docker-compose exec web python manage.py load_order
