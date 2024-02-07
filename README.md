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
