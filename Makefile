# Makefile
IMAGE = archery-target-detection-img
IMAGE_TAG = latest
CONTAINER = archery-target-detection

.PHONY: build run dev clean test stop logs

build:
	docker build -t $(IMAGE):$(IMAGE_TAG) .

build-no-cache:
	docker build --no-cache -t $(IMAGE):$(IMAGE_TAG) .

run:
	docker run --rm -it --name $(CONTAINER) $(IMAGE):$(IMAGE_TAG)

dev:
	docker run --rm -it --name $(CONTAINER) \
		--mount type=bind,source=./,target=/usr/src/app \
		-p 8000:8000 \
		$(IMAGE):$(IMAGE_TAG) bash

run-bg:
	docker run -d --name $(CONTAINER) \
		-p 8000:8000 \
		$(IMAGE):$(IMAGE_TAG)

stop:
	docker stop $(CONTAINER) || true
	docker rm $(CONTAINER) || true

logs:
	docker logs $(CONTAINER)

clean:
	docker rmi $(IMAGE):$(IMAGE_TAG) || true
	docker system prune -f

test:
	docker run --rm $(IMAGE):$(IMAGE_TAG) pytest
