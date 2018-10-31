# build many sites in single vhost/host

before going down, google Nginx.

# brief


### create from local

```
cd [[my_git_source_root]]

docker build --target quickstart -t vhc_quickstart ./sphinx

docker build --target gen-all-html -t vhc_gen_html ./sphinx

docker build --target clean-all-html -t vhc_clean_all ./sphinx

docker build --target gen-nginx-config -t vhc_config_nginx ./sphinx

docker build --target nginx-service -t vhc_nginx_service ./sphinx

```

### create from github

```
docker build --target quickstart -t vhc_quickstart https://github.com/lua511/build-vhost-use-docker.git#master:sphinx

docker build --target gen-all-html -t vhc_gen_html https://github.com/lua511/build-vhost-use-docker.git#master:sphinx

docker build --target clean-all-html -t vhc_clean_all https://github.com/lua511/build-vhost-use-docker.git#master:sphinx

docker build --target gen-nginx-config -t vhc_config_nginx https://github.com/lua511/build-vhost-use-docker.git#master:sphinx

docker build --target nginx-service -t vhc_nginx_service https://github.com/lua511/build-vhost-use-docker.git#master:sphinx
```

### e.g. push to docker hub


#### tag
```
docker tag vhc_quickstart lua511/vhc_quickstart

docker tag vhc_gen_html lua511/vhc_gen_html

docker tag vhc_clean_all lua511/vhc_clean_all

docker tag vhc_config_nginx lua511/vhc_config_nginx

docker tag vhc_nginx_service lua511/vhc_nginx_service
```

#### push

```
docker push lua511/vhc_quickstart

docker push lua511/vhc_gen_html

docker push lua511/vhc_clean_all

docker push lua511/vhc_config_nginx

docker push lua511/vhc_nginx_service
```

# how to use

## init new site

```
docker run --rm -it -v ${YOUR_PROJECT_ROOT}/${YOUR_DOMAIN_ROOT}:/data lua511/vhc_quickstart

```

## gen nginx sites config

```
docker run --rm -v${PROJECT_ROOT}:/wwwroot -v${PROJECT_ROOT}/wconfig:/wwwconfig lua511/vhc_config_nginx
```

## gen html

```
docker run --rm -v ${PROJECT_ROOT}:/wwwroot lua511/vhc_gen_html
```

## start nginx service

```
docker run -d --rm -v ${PROJECT_ROOT}:/wwwroot -v ${PROJECT_ROOT}/wconfig:/wwwconfig -p 80:80 -p 443:443 lua511/vhc_nginx_service
```