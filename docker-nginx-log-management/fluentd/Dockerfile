FROM fluent/fluentd:latest

MAINTAINER Vivek Aggarwal

# Install fluent plugin for S3
RUN gem install fluent-plugin-s3


WORKDIR /fluentd/etc

# Add fluent.conf file
ADD https://raw.githubusercontent.com/viveknangal/honestbee2018/master/docker-nginx-log-management/fluentd/fluentd.conf .

RUN chmod 644 fluentd.conf

ENTRYPOINT ["/usr/bin/fluentd","-c","/fluentd/etc/fluentd.conf","-v"]
