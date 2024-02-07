FROM ubuntu:latest

# Dependencies
RUN apt-get update && apt-get install -y supervisor

# Config(s)
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /var/log/supervisor /my-apps 
RUN ln -s /var/log/supervisor /my-apps
WORKDIR /my-apps

# Program(s)
COPY bash-date/date.sh ./bash-date/date.sh

# Entrypoint
CMD ["/usr/bin/supervisord"]
