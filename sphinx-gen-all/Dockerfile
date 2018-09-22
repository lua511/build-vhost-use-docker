FROM ubuntu:14.04
ARG DEBIAN_FRONTEND=noninteractive
COPY requirements.txt /tmp
COPY gen_all.py /tmp
VOLUME /wwwroot
WORKDIR /tmp
RUN apt-get update && apt-get install -y python3 python3-pip && pip3 install -r /tmp/requirements.txt
ENTRYPOINT python3 gen_all.py && sh make_all.sh