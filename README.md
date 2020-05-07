# NiFi Sandbox

Playground for experimenting with [Apache NiFi](https://nifi.apache.org).

You can start a single-node NiFi cluster and NiFi Registry using [Docker Compose](https://docs.docker.com/compose):

    docker-compose -f docker/docker-compose.yaml up -d

NiFi will be available at [http://localhost:8080/nifi](http://localhost:8080/nifi).

And the registry will be available at [http://localhost:18080/nifi-registry](http://localhost:18080/nifi-registry).
