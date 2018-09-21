# build many sites in single vhost/host

before going down, google Nginx.

**BEST PRACTIC OF THIS ARTICLE:**

```
export PROJ_GIT_ROOT=[[YOUR_PROJECT_ROOT]]
# then keep use this shell
# just copy the following commands and paste
```

#steps

## 1. clone this repo OR JUST follow the steps in this readme.md

*PROJECT_ROOT is your root directory,the top of this repo on local disk.*

```
cd ${PROJECT_ROOT}
git clone git@github.com:lua511/build-vhost-use-docker.git build-vhost-use-docker


# as best practice, we export the root
export PROJ_GIT_ROOT=${PROJECT_ROOT}/build-vhost-use-docker

```

## 2. prepare docker images

### 1. sphinx

```
docker build -t sphinx https://github.com/lua511/build-vhost-use-docker.git:sphinx
```

or from local:

```
docker build -t sphinx ./sphinx
```

### 2. gen-nginx-sites

```
docker build -t gen-nginx-sites https://github.com/lua511/build-vhost-use-docker.git:gen-nginx-sites
```

or from local:

```
docker build -t gen-nginx-sites ./gen-nginx-sites
```

### 3. nginx

```
docker build -t nginx https://github.com/lua511/build-vhost-use-docker.git:nginx
```

or from local:

```
docker build -t nginx ./nginx
```


if your like,google some information about sphinx

## 3. place some site under wwwroot

*liuan.blog is your*

### 1. create directory

```
cd ${PROJ_GIT_ROOT}
cd wwwroot
mkdir liuan.blog
```

### 2. init site as need

```
docker run --rm -it -v ${PROJECT_ROOT}/wwwroot/liuan.blog:/data -w /data sphinx sphinx-quickstart
```

### 3. build site as need

```
docker run --rm -v ${PROJECT_ROOT}/wwwroot/liuan.blog:/data -w /data sphinx make html
```

## 4. place another site under wwwroot

do same thing as `3. place some site under wwwroot`

## 6. generate config

```
docker run --rm -v ${PROJECT_ROOT}/wwwroot:/wwwroot -v ${PROJECT_ROOT}/wwwcfg:/wwwconfig gen-nginx-sites
```

## 7. start nginx service

```
docker run -d --rm -v ${PROJECT_ROOT}/wwwroot:/wwwroot -v ${PROJECT_ROOT}/wwwcfg:/wwwconfig -p 80:80 -p 443:443 nginx
```



# hint

the vhost is setup completed. DO REMEMBER set your hosts DNS.