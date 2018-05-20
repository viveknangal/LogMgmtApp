FROM fluent/fluentd:latest

MAINTAINER Vivek Aggarwal

# Install fluent plugin for S3
RUN gem install fluent-plugin-s3


WORKDIR /fluentd/etc

# Add fluent.conf file
COPY fluentd.conf .

ENTRYPOINT ["/usr/bin/fluentd","-c","/fluentd/etc/fluentd.conf","-v"]
