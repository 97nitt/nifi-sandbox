## Bootstrap Container

The Docker image defined in this folder executes a [Python script](python/bootstrap.py) that applies some bootstrap 
configuration once NiFi is up and running:

- adds NiFi Registry client

To run this script locally, create a Python 3.6+ virtual environment and install dependencies:

    $ python -m venv .venv --prompt nifi-sandbox
    $ source .venv/bin/activate
    $ pip install -r docker/nifi-bootstrap/python/requirements.txt
