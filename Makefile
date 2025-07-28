DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app
MESSAGE_FILE = docker_compose/messaging.yaml
STORAGES_FILE = docker_compose/storages.yaml

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: message
message:
	${DC} -f ${MESSAGE_FILE} ${ENV} up --build -d

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up --build -d

.PHONY: all
all:
	${DC} -f ${STORAGES_FILE} -f ${APP_FILE} -f ${MESSAGE_FILE} ${ENV} up --build -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: message-logs
message-logs:
	${DC} -f ${MESSAGE_FILE} logs

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} down

.PHONY: message-down
message-down:
	${DC} -f ${MESSAGE_FILE} down

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} down

.PHONY: app-shell
app-shell:
	${EXEC} ${APP_CONTAINER} bash


.PHONY: test
test:
	${EXEC} ${APP_CONTAINER} pytest