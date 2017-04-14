### Deploying Jenkins
ICESI University  
Course: Distributed Systems  
Professor: Daniel Barragán C.  
Topic: Jenkins and system settings  
E-mail: daniel.barragan at correo.icesi.edu.co


### Objectives
* Do self-provisioning of jenkins master settings

### Steps

Create a config.json file

``` json

```

Create a Dockerfile

```

```

Build the image

```

```

Create a docker container from the image

```
$ docker run -d -p 8080:8080 --name jenkins-master jenkins:2.19.2
```

Go to http://127.0.0.1:8080 in your browser



Destroy the container

```
$ docker rm jenkins-master -f
```

### References
https://hub.docker.com/_/jenkins/
