FROM nginx:latest

MAINTAINER Vivek Aggarwal

WORKDIR /usr/share/nginx/html

# Add Index.html to the Workspace
COPY index.html .

CMD ["nginx","-g","daemon off;"]
