FROM ubuntu:latest

# Dependencies
RUN apt-get update && apt-get install -y supervisor nano tree
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip paho-mqtt

# Config(s)
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /var/log/supervisor /my-apps 
RUN ln -s /var/log/supervisor /my-apps
WORKDIR /my-apps

# Program(s)
COPY bash-date ./bash-date
COPY mqtt-broker ./mqtt-broker

# Entrypoint
CMD ["/usr/bin/supervisord"]
