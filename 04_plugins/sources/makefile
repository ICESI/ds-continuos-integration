build:
	@docker build -t jenkins-master:2.19.2 .
run:
	@docker run -d -p 8080:8080 -p 50000:50000 --name=jenkins-master jenkins-master:2.19.2
start:
	@docker start jenkins-master
stop:
	@docker stop jenkins-master
clean:
	@docker rm jenkins-master -f
