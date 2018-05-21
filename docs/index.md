# Welcome to docker-machine-py

!!! Version
    This version is under development. checkout open issues


<p align="center">
  <img src="https://camo.githubusercontent.com/439d0ad6ea1a65694cfc66c537b6b22e1ae1fd01/68747470733a2f2f646f63732e646f636b65722e636f6d2f6d616368696e652f696d672f6c6f676f2e706e67"/>
</p>

A **simple** but **powerful** docker-machine wrapper for **Python 3.6**

Machine lets you create Docker hosts on your computer, on cloud providers, and inside your own data center. It creates servers, installs Docker on them, then configures the Docker client to talk to them.

It works like this for simple machine deployment:

## Examples

### Default machine creation

```python
manager.create_default()
manager.start()
```

### Read status of machine 'my_machine'

```python
status = manager.status("my_machine")
```

### Get configuration of machine 'my_machine'

```python
config = manager.config("my_machine")
```

### Stop a machine called 'my_machine'

```python
manager.stop("my_machine")
```