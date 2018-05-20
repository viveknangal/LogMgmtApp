# Dockerized Nginx-Fluentd Log Management Application
This is a Dockerized Ngnix Application running serving static content at port no 9000

Another container having Fluentd installed is deployed to publish logs to AWS S3 bucket

**docker-compose** is used under the hood to spin both these containers


## Prerequisite to run this Application
* **Docker** and **docker-compose** should to be installed
* **AWS_ACCESS_KEY_ID** and **AWS_SECRET_ACCESS_KEY** attributes should be provided in the docker-compose.yml.This is required for  publishing Nginx logs to AWS S3.
* Nginx application is exposed on host machine on port number 9000

 ## Directory structure
Details of directory contents for this application
```
 docker-nginx-log-management
   ├── docker-compose.yml ---> Used to provision two seperate containers one for Nginx & other for Fluentd
   ├── fluentd
   │   ├── Dockerfile -------> Used for creating fluentd container 
   │   └── fluentd.conf -----> Fluentd conf file having configuration for capturing docker logs to S3
   └── nginx
       ├── Dockerfile -------> Used for creating nginx container
       └── index.html -------> Custom Welcome Page for Nginx
```

## How to run this application

To run application in foreground ,run below command:-
```sh
$ docker-compose up
```
## Expected Output
Above **docker-compose up** will start publishing the logs(compressed format i.e gz)  to S3 bucket as specfied in **fluentd.conf** file 
