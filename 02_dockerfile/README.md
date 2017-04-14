### Deploying Jenkins
ICESI University  
Course: Distributed Systems  
Professor: Daniel Barragán C.  
Topic: Jenkins and Dockerfile  
E-mail: daniel.barragan at correo.icesi.edu.co


### Objectives
* Customise Jenkins image with a Dockerfile

### Steps

Create a Dockerfile

```
FROM jenkins:2.19.2

ENV JAVA_OPTS="\
 -Dhudson.footerURL=https://hub.docker.com/_/jenkins/\
 -Djenkins.install.runSetupWizard=false"
```

Build an image from the Dockerfile

```
$ docker build -t jenkins-master:2.19.2 .
```

Create a docker container from the image

```
$ docker run -d -p 8080:8080 --name jenkins-master jenkins-master:2.19.2
```

Go to http://127.0.0.1:8080 in your browser

![][1]

Destroy the container

```
$ docker rm jenkins-master -f
```

### References
https://hub.docker.com/_/jenkins/

[1]: images/01_jenkins_welcome.png
