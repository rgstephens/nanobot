-include .env
REGISTRY   ?= $(error REGISTRY is not set. Add REGISTRY=your.registry.host to .env)
IMAGE      := $(REGISTRY)/nanobot
VERSION    := $(shell cat VERSION)
BUILD_DATE := $(shell date -u +"%Y-%m-%d")
PLATFORMS  := linux/amd64,linux/arm64
BUILDER    := multiarch

TAGS := -t $(IMAGE):$(VERSION) -t $(IMAGE):latest

BUILD_ARGS := \
	--build-arg VERSION=$(VERSION) \
	--build-arg BUILD_DATE=$(BUILD_DATE)

.PHONY: docker-login docker-setup docker-build-all docker-push-all docker-release version

version:
	@echo $(VERSION)

docker-login:
	docker login $(REGISTRY)

# Create the multi-platform builder if it doesn't already exist
docker-setup:
	docker buildx inspect $(BUILDER) > /dev/null 2>&1 || \
		docker buildx create --name $(BUILDER) --driver docker-container --use
	docker buildx use $(BUILDER)

docker-build-all: docker-setup
	docker buildx build \
		--builder $(BUILDER) \
		--platform $(PLATFORMS) \
		$(BUILD_ARGS) \
		$(TAGS) \
		.

docker-push-all: docker-setup
	docker buildx build \
		--builder $(BUILDER) \
		--platform $(PLATFORMS) \
		$(BUILD_ARGS) \
		$(TAGS) \
		--push \
		.

docker-release: docker-push-all
	@echo "Released $(IMAGE):$(VERSION)"
	crane ls $(REGISTRY)/nanobot
