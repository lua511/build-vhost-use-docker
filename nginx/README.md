# build image

```
docker build -t nginx .
```

# build from github

```
docker build -t nginx https://github.com/lua511/build-vhost-use-docker.git:nginx

```

## for vhost
*vhost is another project which is supported by build-vhost-use-docker/this_repo*

```
docker build -t vhc_nginx https://github.com/lua511/build-vhost-use-docker.git#master:nginx
docker tag vhc_nginx lua511/vhc_nginx
docker push lua511/vhc_nginx
```