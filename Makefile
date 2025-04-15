run:
	docker compose up -d --remove-orphans

stop:
	docker compose down

docker_build:
	docker build -t d2r-charactersheet_img .

docker_run:
	docker run -d --name d2r-charactersheet -p 8000:8000 d2r-charactersheet_img

docker_restart:
	docker container stop d2r-charactersheet && \
	docker container rm d2r-charactersheet && \
	docker run -d --name d2r-charactersheet -p 8000:8000 d2r-charactersheet_img