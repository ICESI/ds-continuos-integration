### Deploying Jenkins
ICESI University  
Course: Distributed Systems  
Professor: Daniel Barragán C.  
Topic: Intro to Docker and Jenkins
E-mail: daniel.barragan at correo.icesi.edu.co


### Objectives
* Create a jenkins master container

### Steps

Get last docker image from dockerhub

```
$ docker pull jenkins:2.19.2
```

Create a docker container from the downloaded image

```
$ docker run -d -p 8080:8080 --name jenkins-master jenkins:2.19.2
```

Go to http://127.0.0.1:8080 in your browser

![][1]

Destroy the container

```
$ docker rm jenkins-master -f
```

### References
https://hub.docker.com/_/jenkins/
<!-- https://hub.docker.com/r/jenkinsci/jenkins/ -->

[1]: images/01_jenkins_wizard.png
