build:
	docker-compose build

test:
	docker-compose run --rm --entrypoint=pytest bot

start:
	docker-compose run --rm --service-ports bot

push:
	docker push joanfont/santantoni