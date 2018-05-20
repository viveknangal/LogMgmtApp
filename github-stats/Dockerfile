FROM python:2.7-alpine3.7
MAINTAINER Vivek Aggarwal
WORKDIR /opt
# Add Python Script to the Workspace
ADD https://raw.githubusercontent.com/viveknangal/honestbee2018/master/github-stats/github-script.py .
# Add Python packages dependency resolver to the Workspace
ADD https://raw.githubusercontent.com/viveknangal/honestbee2018/master/github-stats/requirements.txt .
# Passing the ENV variables for the Input & Output file
ENV input_file_name=$input_file output_file_name=$output_file
RUN chmod u+x github-script.py && \
    pip install -r requirements.txt
ENTRYPOINT exec /opt/github-script.py $input_file_name $output_file_name
