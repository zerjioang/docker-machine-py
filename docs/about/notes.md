# Releate notes

![docker-image](https://cdn-images-1.medium.com/max/2000/1*PCfipbEQTl6TLTGppEvUZA.png)

This initial version of **docker-machine** wrapper has most of its basic functionality coverered with unit tests.
However, this is still initial version. A development work is still missing on it, so dont worry if you miss something, just ask for it via GITHUB issue and collaborate!

!!! info
    Current version: **0.0.1**

## Release notes of **0.0.1**

* Automatically lookup for **docker-machine** binary if not found on usual path.
* Automatically creates a **default** machine if not exists.
* Added support for docker swarm configuration fetch.
* Added support for **docker-machine** simple commands:
    * version
    * url
    * upgrade
    * stop
    * status
    * start
    * ip
    * inspect
    * help
    * env
    * create
    * config

