FROM ubuntu:14.04
ARG DEBIAN_FRONTEND=noninteractive
COPY requirements.txt /tmp
RUN apt-get update && apt-get install -y python3 python3-pip && pip3 install -r /tmp/requirements.txt
VOLUME /data