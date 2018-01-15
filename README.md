## Simple-RestAPI

#### 1. Checkout source code from Github
```sh
$ mkdir simple-restapi
$ cd simple-restapi
$ git clone git@github.com:dtphuc/Simple-RestAPI.git .
```

#### 2. Run the command on top of directory
```sh
$ docker-compose up -d
```

#### 3. Check the container is up
```sh
$ docker ps -a
CONTAINER ID | IMAGE|COMMAND|CREATED|STATUS|PORTS|NAMES
f2abff807b99 | php:apache | "docker-php-entryp..." | 5 minutes ago | Up 5 minutes | 0.0.0.0:20040->80/tcp | simplerestapi_website_1

27f62aabc62c | simplerestapi_simple-python | "python3 api.py" | 5 minutes ago | Up 5 minutes | 0.0.0.0:20030->80/tcp | simplerestapi_simple-python_1
```

#### 4. Test RestAPI with curl command
```sh
$ curl localhost:20040 | jq '.'
```
The output like

[
  "Dang Thanh Phuc",
  "Age - 27",
  "Github: https://github.com/dtphuc"
]
