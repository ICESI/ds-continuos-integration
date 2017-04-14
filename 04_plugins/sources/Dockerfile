FROM jenkins:2.19.2

COPY config.json /tmp/config.json
COPY parse_plugins.py /tmp/parse_plugins.py

RUN /usr/local/bin/install-plugins.sh $(python /tmp/parse_plugins.py)

ENV JAVA_OPTS="\
 -Dhudson.footerURL=https://hub.docker.com/_/jenkins/\
 -Djenkins.install.runSetupWizard=false"
