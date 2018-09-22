# readme.md

# build image
```
docker build -t gen-nginx-sites .
```

# build from github

```
docker build -t gen-nginx-sites https://github.com/lua511/build-vhost-use-docker.git#master:gen-nginx-sites
```

## for vhost
*vhost is another project which is supported by build-vhost-use-docker/this_repo*

```
docker build -t vhc_gen_cfg https://github.com/lua511/build-vhost-use-docker.git#master:gen-nginx-sites
docker tag vhc_gen_cfg lua511/vhc_gen_cfg
docker push lua511/vhc_gen_cfg
```