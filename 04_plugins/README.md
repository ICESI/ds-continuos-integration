### Deploying Jenkins
ICESI University  
Course: Distributed Systems  
Professor: Daniel Barragán C.  
Topic: Jenkins and Plugins  
E-mail: daniel.barragan at correo.icesi.edu.co


### Objectives
* Do self-provisioning of jenkins master plugins

### Steps

Create a file config.json

``` json
{
	"plugins": {
		"locale": "1.2",
		"github": "1.22.3",
		"workflow-aggregator": "2.4",
		"ghprb": "1.33.1",
		"ansicolor": "0.4.2",
		"github-oauth": "0.24",
		"saferestart": "0.3"
	}
}
```

Create a file parse_plugins.py

``` python
import json
import string

with open('config.json') as config_file:    
  data = json.load(config_file)
plugin_array = [ k+":"+v for k, v in data["plugins"].items() ]
plugin_list = ' '.join([str(x) for x in plugin_array])
print(plugin_list)
```

Create a Dockerfile

```
FROM jenkins:2.19.2

COPY config.json /tmp/config.json
COPY parse_plugins.py /tmp/parse_plugins.py

RUN /usr/local/bin/install-plugins.sh $(python /tmp/parse_plugins.py)

ENV JAVA_OPTS="\
 -Dhudson.footerURL=https://hub.docker.com/_/jenkins/\
 -Djenkins.install.runSetupWizard=false"
```

Build the image

```
$ docker build -t jenkins-master:2.19.2 .
```

Create a docker container from the image

```
$ docker run -d -p 8080:8080 --name jenkins-master jenkins-master:2.19.2
```

Go to http://127.0.0.1:8080/pluginManager/installed in your browser and
verify plugins has been installed

![][1]

Destroy the container

```
$ docker rm jenkins-master -f
```

### References
https://hub.docker.com/_/jenkins/

[1]: images/01_jenkins_plugins.png
