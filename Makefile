build:
	docker-compose build

start:
	docker-compose run --rm --service-ports bot

push:
	docker push joanfont/santantoni