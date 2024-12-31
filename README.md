a simply python script to capture the screenshot of a webpage

the docker image can be downloaded from [dockerhub](https://hub.docker.com/r/arthurtsang/myscreenshot/)

add this to docker compose
```
  myscreenshot:
    image: arthurtsang/myscreenshot
    restart: always
    container_name: myscreenshot
    ports:
      - 5050:5000
```

and you can set the Generic screenshot API in NextCloud Bookmark to
```
http://host.docker.internal:5050/screenshot?url={url}
```