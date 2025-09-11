# Makefile
IMAGE = archery-target-detection-img
IMAGE_TAG = latest
CONTAINER = archery-target-detection

.PHONY: build run

build:
	docker build -t $(IMAGE):$(IMAGE_TAG) .

run:
	docker run --rm -it --name $(CONTAINER) $(IMAGE):$(IMAGE_TAG) 

dev:
	docker run --rm -it --name $(CONTAINER) --mount type=bind,source=./,target=/usr/src/app $(IMAGE):$(IMAGE_TAG) bash
