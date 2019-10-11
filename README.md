# dockme

[![Build Status](https://travis-ci.com/kmayerb/dockme.svg?branch=master)](https://travis-ci.com/kmayerb/dockme)

a minimal python package with one dependency to be containerized


```bash
python transform_list.py --input ${input_filename} --output ${output_filename}
```

## Adventures in Containerization

1. Create a python3 image, with specific dependencies (numpy), and copying our package files.

Dockerfile:

```
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

```

Build
```bash
docker build -t dockme .
```

After the build:
```bash
docker run -it dockme
```

We see immediately that our dependencies not present in the base image python:3
are available.
```
Python 3.7.4 (default, Sep 12 2019, 15:40:15) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information. 
>>> import numpy
```

Our folder structure is available:
```
Python 3.7.4 (default, Sep 12 2019, 15:40:15) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information. 
>>> from dockme import transform
>>> transform._log10_transform(1000.0)
```

Here is some more info about our container, which was build with '4.9.184-linuxkit'
```
>>> import os
>>> os.uname()
posix.uname_result(sysname='Linux', nodename='eb3e17473e6a', release='4.9.184-linuxkit', version='#1 SMP Tue Jul 2 22:58:16 UTC 2019', machine='x86_64')
>>> os.path.abspath(".")
'/usr/src/app'
```




