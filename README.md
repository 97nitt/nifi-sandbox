# NiFi Sandbox

Playground for experimenting with [Apache NiFi](https://nifi.apache.org).

You can start a single-node NiFi cluster and NiFi Registry using [Docker Compose](https://docs.docker.com/compose):

    docker-compose -f docker/docker-compose.yaml up -d

This will start the following containers (be patient, NiFi takes about a minute to startup):

| Container                               | Description             | URL                                                                          |
|-----------------------------------------|-------------------------|------------------------------------------------------------------------------|
| [nifi](docker/nifi)                     | NiFi                    | [http://localhost:8080/nifi](http://localhost:8080/nifi)                     |
| [nifi-registry](docker/nifi-registry)   | NiFi Registry           | [http://localhost:18080/nifi-registry](http://localhost:18080/nifi-registry) |
| [nifi-bootstrap](docker/nifi-bootstrap) | Bootstrap configuration | n/a                                                                          |
