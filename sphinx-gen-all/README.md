README.md
=========

a docker image for init & generate sphinx-markdown site.

## create sphinx docker image

```
# create image
cd sphinx-docker
docker build -t sphinx-gen-all .
```


## create from github

```
docker build -t sphinx https://github.com/lua511/build-vhost-use-docker.git:sphinx-gen-all
```


## how to use

```
docker run --rm -it -v ${PROJECT_ROOT}:/wwwroot temp
```


## for vhost
*vhost is another project which is supported by build-vhost-use-docker/this_repo*

```
docker build -t vhc_gen_html https://github.com/lua511/build-vhost-use-docker.git#master:sphinx-gen-all
docker tag vhc_gen_html lua511/vhc_gen_html
docker push lua511/vhc_gen_html
```
