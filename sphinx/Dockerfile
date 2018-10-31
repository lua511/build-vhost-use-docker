FROM ubuntu:16.04 as ubuntu-chinese
ENV LANG C.UTF-8

FROM ubuntu-chinese as sphinx-base
ADD resources /wdir
RUN export DEBIAN_FRONTEND="noninteractive" && apt-get -y update && apt-get install -y python3 curl make && curl https://bootstrap.pypa.io/get-pip.py | python3 && rm -rf /var/lib/apt/lists/* && pip3 install -r /wdir/requirements.txt

FROM sphinx-base as quickstart
VOLUME /data
WORKDIR /data
ENTRYPOINT sphinx-quickstart

FROM sphinx-base as gen-all-html
VOLUME /wwwroot
WORKDIR /wdir
ENTRYPOINT python3 gen_all.py && sh make_all.sh

FROM sphinx-base as clean-all-html
VOLUME /wwwroot
WORKDIR /wdir
ENTRYPOINT python3 gen_all.py && sh clean_all.sh

FROM sphinx-base as gen-nginx-config
VOLUME /wwwroot
VOLUME /wwwconfig
WORKDIR /wdir
ENTRYPOINT python3 find_host.py

FROM ubuntu-chinese as nginx-service
VOLUME /wwwroot
VOLUME /wwwconfig
VOLUME /var/log/nginx

ARG DEBIAN_FRONTEND=noninteractive
RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d \
    && apt-get update \
    && apt-get install -y nginx \
    && rm -rf /etc/nginx/sites-available && ln -s /wwwconfig /etc/nginx/sites-available \
    && rm -rf /etc/nginx/sites-enabled && ln -s /wwwconfig /etc/nginx/sites-enabled \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]