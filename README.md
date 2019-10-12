# dockme

[![Build Status](https://travis-ci.com/kmayerb/dockme.svg?branch=master)](https://travis-ci.com/kmayerb/dockme)

A minimal python package with a few dependencies to illustrate containerization.

## The Code-Container-CI Trinity

By the end of this process, we will have set up three-mutually interacting development units. Together, theymwill allow us to test changes as we develop a python package.

1. A GitHub Repo - the python package and a Dockerfile

2. A DockerHub Repo or Quay.io Repo - builds the docker image on each GitHub push

3. Travis-CI - builds the project from a DockerHub image and runs tests.

4. ReadTheDocs.org - While not part of the CCC-trinity, this will provide up to data documentation of the project.


## Python Containerization for Scientific Research

With so many docker images floating in the ether, which base image should we use as a  starting point for a general scientific python project? On the one hand, there are some pre-built docker images, compliete with all the bells and whistles (see: e.g., Jupyter Containers). Assuming we don't care about container size, these might be a fine choice, but here we focus on building a small custom container for a our python 3.7 package?

Let's define what we want:

* Mimic a local linux python environment where we can't use docker containers, due to security vulnerabilites.
* get linux appications using apt-get.
* add python dependencies from active GitHub repos with `pip install` 
* be accessible to NextFlow

1. Offical Python Containers and Pip.

Because we care more about specifying a specific version of python, we use an official python container from dockerhub specifying a tag for one built on the  Debian GNU / Linux 10 OS. 

#### Pulling the Base Image from DockerHub

```bash
MBP:~ user$ docker pull python:3.7.4-buster
MBP:~ user$ run -it python:3.7.4-buster bin/bash
```
```bash
root@6f7e41abfb09:/# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 10 (buster)"
NAME="Debian GNU/Linux"
VERSION_ID="10"
VERSION="10 (buster)"
```
Check python3 version, which is devoid of scientific dependencies
```bash
root@6f7e41abfb09:/# python3
Python 3.7.4 (default, Sep 12 2019, 15:40:15) 
[GCC 8.3.0] on linux
>>> import pandas
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pandas'
```




2. What about an Anaconda Containers?


3. What about biocontainers?

These come in a number of flavors 


## What are the benefits of using biocontainers?







```bash
python transform_list.py --input ${input_filename} --output ${output_filename}
```

## Early Adventures in Containerization

### 1. A Python Contanier with Specific Dependencies

Create a python3 image, with specific dependencies (numpy), and copying our package files.

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

#### Mounting 

Using volumes flag we can connect the local directory ${HOME}/foo to 
the directory /foo in the container. (Note that container ddid not previously contain this directory)

```bash
cd 
mkdir foo
docker run -it -v ${HOME}/foo:/foo dockme
Python 3.7.4 (default, Sep 12 2019, 15:40:15) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.system("python3 transform_list.py --input input.txt --output /foo/foo_output.txt")
```
The output file from the container is now accessible in our local machine.










