# Algo API

## Description

#### Services and tools
|  Service | Purpose  |
|---|---|
| algo-api | The main application that exposes the API |
| loadgen | A sample app to simulate load on the API (idea taken from [here](https://github.com/GoogleCloudPlatform/microservices-demo)) |
| prometheus | For collectiong metrics |
| grafana | For visualization of metrics |


## Build and run
```console
docker-compose build
docker-compose up -d
```

Once application starts the `loadgen` will start randomly query available endpoints which will allow to visialize some data in monitoring.

##### API Documentantion
Documentation is autogenerated and can be found under http://localhost:8000/docs

## Monitoring
As mentioned above monitroing is done with Prometheus and it's visilaied via Grafana.
There is already configured Grafana dashboard with some basic metrics, like QPS and HTTP Latency.
The configured dashboard is called "Algorithms API"
(I'm sending the `.grafana` folder which stores the Grafana database)

Grafana can be accessed under http://localhost:3000/
username/password - admin/admin

## Run the tests in docker
```console
docker-compose run --rm algo-api poetry run pytest ./
```
- There are some shortcuts in Makefile which I used on my local.

### TO-DO

- [ ] Multistage build for smaller image
- [ ] Extend test for API for other routes
- [ ] Find a way to register new function by avoiding too much copy/pasting
- [ ] Avoid hardcoding config parameters e.g. pushgateway
