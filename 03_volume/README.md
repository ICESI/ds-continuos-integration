### Deploying Jenkins
ICESI University  
Course: Distributed Systems  
Professor: Daniel Barragán C.  
Topic: Jenkins and volumes
E-mail: daniel.barragan at correo.icesi.edu.co


### Objectives
* Store Jenkins files outside container

### Steps

Create a docker container from the image

```
$ docker run -d -p 8080:8080 --name jenkins-master jenkins:2.19.2
```

Go to http://127.0.0.1:8080 in your browser and create a freestyle job

---

Destroy the container

```
$ docker rm jenkins-master -f
```

Create the container again

```

```

Go to http://127.0.0.1:8080 in your browser and check that freestyle job still exist

### References
https://hub.docker.com/_/jenkins/
