# Supervisord-Playground

Aim: use supervisord to manage applications/scripts

Supervisord was chosen over systemd due to compatibility with containers. 

## Build and run
```
docker build -t mysupervisord . && docker run -i -t --name mysupd mysupervisord
```

#### Build container
```
docker build -t mysupervisord .
```

#### Run container
```
docker run -i -t --name mysupd mysupervisord
```

### Join container
```
docker exec -it mysupd bash
```

## Apps

| App | Description |
| --- | ----------- |
|[bash-date](bash-date)|Call linux date command for supervisord logging to file|
