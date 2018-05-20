FROM nginx:latest

MAINTAINER Vivek Aggarwal

WORKDIR /usr/share/nginx/html

# Add Index.html to the Workspace
ADD https://raw.githubusercontent.com/viveknangal/honestbee2018/master/docker-nginx-log-management/nginx/index.html .

RUN chmod 644 index.html

CMD ["nginx","-g","daemon off;"]
