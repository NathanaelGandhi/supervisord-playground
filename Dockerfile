FROM ubuntu:latest

# Dependencies
RUN apt-get update && apt-get install -y supervisor 
RUN apt-get install -y python3-pip iproute2 can-utils
RUN pip install --upgrade pip python-can

# Config(s)
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /var/log/supervisor /my-apps 
RUN ln -s /var/log/supervisor /my-apps
WORKDIR /my-apps
## Enable the vcan kernel module
# RUN modprobe vcan
## Create the virtual CAN interface
# RUN ip link add dev vcan0 type vcan

# Program(s)
COPY bash-date/date.sh ./bash-date/date.sh
COPY py-vcan-pub/py-vcan-pub.py ./py-vcan-pub/py-vcan-pub.py

# Entrypoint
CMD ["/usr/bin/supervisord"]
