README.md
=========

a docker image for init & generate sphinx-markdown site.

## create sphinx docker image

```
# create image
cd sphinx-docker
docker build -t sphinx .
```


### precheck

```
# check image exists
docker image list | grep "sphinx"
```

```
# delete an old image
docker image rm sphinx
```


## create from github

```
docker build -t sphinx https://github.com/lua511/build-vhost-use-docker.git:sphinx
```

## for vhost
*vhost is another project which is supported by build-vhost-use-docker/this_repo*

```
docker build -t vhc_sphinx https://github.com/lua511/build-vhost-use-docker.git#master:sphinx
docker tag vhc_sphinx lua511/vhc_sphinx
docker push lua511/vhc_sphinx
```