# Algo API

## Description

#### Services and tools
|  Service | Purpose  |
|---|---|
| algo-api | The main application that exposes the API |
| loadgen | A sample app to simulate load on the API (idea taken from [here](https://github.com/GoogleCloudPlatform/microservices-demo)) |
| prometheus | For collectiong data |
| grafana | For visualization |


## Build and run
```console
docker-compose build && docker-compose up
```

## Run the tests in docker
```console
docker-compose run --rm algo-api poetry run pytest ./
```
- There are some shortcuts in Makefile which I used on my local.

### TO-DO

- Multistage build for smaller image
- Extend test for API for other routes
- Find a way to register new function by avoiding too much copy/pasting
- Avoid hardcoding config parameters for pushgateway
