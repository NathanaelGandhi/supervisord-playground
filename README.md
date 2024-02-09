# Supervisord-Playground

Aim: use supervisord to manage applications/scripts

Supervisord was chosen over systemd due to compatibility with containers. 

## Build and run
```
docker build -t supervisord-playground . && docker run -i -t --name supdpg --rm supervisord-playground
```

#### Build container
```
docker build -t supervisord-playground .
```

#### Run container
```
docker run -i -t --name supdpg --rm supervisord-playground
```

### Join container
```
docker exec -it supdpg bash
```

## Apps

| App | Description |
| --- | ----------- |
|[bash-date](bash-date)|Call linux date command for supervisord logging to file|


## Notes

### Other Containers
- docker run -it -p 1883:1883 -p 9001:9001 -v mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
