
.PHONY: help
help:
	@echo "Makefile arguments"
	@echo ""
	@echo "Makefile commands:"
	@echo "build  -> builds both containers"
	@echo "run    -> runs both containers"
	@echo "net    -> create network for containers communication"


.PHONY: build
build:
	@docker build -t foobar-foo:latest foo/
	@docker build -t foobar-bar:latest bar/

.PHONY: net
net:
	@docker network create foobar-dev_default

.PHONY: run
run:
	@docker run -d -e LIS_IP='0.0.0.0' -e LIS_PORT='4000' -e BAR_ENDPOINT='bar:4001' --name foo --net foobar-dev_default -p 4000:4000 foobar-foo:latest
	@docker run -d -e LIS_IP='0.0.0.0' -e LIS_PORT='4001' --name bar --net foobar-dev_default -p 4001:4001 foobar-bar:latest
