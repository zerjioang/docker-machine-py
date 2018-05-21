# Docker Machine Wrapper Overview

You can use Python Docker Machine Wrapper to:

* Install and run Docker on Mac, Windows or Linux.
* Provision and manage multiple remote Docker hosts.
* Provision Swarm clusters.

![docker-machine](https://devopscube.com/wp-content/uploads/2015/08/DOCKER-MACHINE.png)

## First things first: what is Docker Machine?

Docker Machine is a tool that lets you install Docker Engine on virtual hosts, and manage the hosts with docker-machine commands. You can use Machine to create Docker hosts on your local Mac or Windows box, on your company network, in your data center, or on cloud providers like Azure, AWS, or Digital Ocean.

Using docker-machine commands, you can start, inspect, stop, and restart a managed host, upgrade the Docker client and daemon, and configure a Docker client to talk to your host.

Point the Machine CLI at a running, managed host, and you can run docker commands directly on that host. For example, run docker-machine env default to point to a host called default, follow on-screen instructions to complete env setup, and run docker ps, docker run hello-world, and so forth.

Machine was the only way to run Docker on Mac or Windows previous to Docker v1.12. Starting with the beta program and Docker v1.12, Docker for Mac and Docker for Windows are available as native apps and the better choice for this use case on newer desktops and laptops. We encourage you to try out these new apps. The installers for Docker for Mac and Docker for Windows include Docker Machine, along with Docker Compose.

If you aren’t sure where to begin, see Get Started with Docker, which guides you through a brief end-to-end tutorial on Docker.

## Install Machine Wrapper directly

1. Install **docker-machine**

```bash
$ base=https://github.com/docker/machine/releases/download/v0.14.0 &&
  curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
sudo install /tmp/docker-machine /usr/local/bin/docker-machine
```

2. Install **docker-machine-py**

```python
pip install docker-machine-py
```

3. Check machine installation with:

```bash
$ docker-machine version
docker-machine version 0.14.0, build 9371605
```

## First interactions

**docker-machine-py** wrapper is designed for Python 3.6+ and thus, it exposed a global variable called **manager** that is the entrypoint for all wrapper interaction. As an example, fetching machine version is shown:
```python

from machine import manager

version = manager.get_version()
print(version)
```

If everything was successful, you will see:

!!! success
    docker-machine version 0.14.0, build 89b8332

### Create a machine using virtualbox driver

Using **docker-machine** cli, this would be:
```bash
docker-machine create --driver virtualbox test
```
Using the **docker-machine-py** wrapper for Python 3.6:
```python
from machine import manager
manager.create("test")
```



