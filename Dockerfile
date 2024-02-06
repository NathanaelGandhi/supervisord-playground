FROM ubuntu:latest

# Dependencies
RUN apt-get update && apt-get install -y supervisor

# Config(s)
RUN mkdir -p /var/log/supervisor /my-apps 
RUN ln -s /var/log/supervisor /my-apps
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Program(s)
COPY bash-date/date.sh my-apps/bash-date/date.sh

# Entrypoint
CMD ["/usr/bin/supervisord"]
