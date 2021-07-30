

# Docker cheat sheet

List all images:
```
$ docker image ls
```

List all containers:
```
$ docker ps -a
```

Remove everything:
```
$ docker system prune -a
```

Get a shell into a Docker image:
```
$ docker run -it --entrypoint bash ubuntu:18.04
```
