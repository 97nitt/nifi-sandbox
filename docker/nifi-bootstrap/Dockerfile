FROM python:3.8-alpine

# copy source code
ADD python /opt/bootstrap

# install dependencies
RUN apk add build-base libffi-dev openssl-dev libxml2-dev libxslt-dev
RUN pip install -r /opt/bootstrap/requirements.txt

# run bootstrap script
ENTRYPOINT ["python", "/opt/bootstrap/bootstrap.py"]
