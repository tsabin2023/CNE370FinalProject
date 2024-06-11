# Database Shard Github

This Docker image runs the 2.4 version of MariaDB MaxScale image: mariadb:10.3, modified into shard architecture with two sharded database.

-	[Travis CI:  
	![build status badge](https://img.shields.io/travis/mariadb-corporation/maxscale-docker/master.svg)](https://travis-ci.org/mariadb-corporation/maxscale-docker/
branches)

- Zak Rubin
  - [MaxScale Docker on GitHub](https://github.com/Zohan/maxscale-docker)

## Running
note the following assumptions are made, you have a machine with a python 3 IDE installed, you know how to pick your IDE python 3 interpreter and install packages in its enviroment, and you have a server with Ubuntu 22.04, know how to access its terminal, and already have Docker and Docker-Compose and installed. https://docs.docker.com/engine/install/ubuntu/
https://docs.docker.com/compose/install/

from your server terminal type/copy and paste

```
get clone https://github.com/tsabin2023/CNE370FinalProject
```
Press enter

[The MaxScale docker-compose setup](./docker-compose.yml) 

~/test1/CNE370FinalProject/maxscale
contains MaxScale
configured with a three node sharded databse. To start it, run the
following commands in this directory.

```
docker-compose build
docker-compose up -d
```

After MaxScale and the servers have started (takes a few minutes), you can find
the readwritesplit router on port 4006 and the readconnroute on port 4008. The
user `maxuser` with the password `maxpwd` can be used to test the cluster.
Assuming the mariadb client is installed on the host machine:
```
$ mysql -umaxuser -pmaxpwd -h 127.0.0.1 -P 4006 test
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 10.2.12 2.2.9-maxscale mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [test]>
```
You can edit the [`maxscale.cnf.d/example.cnf`](./maxscale.cnf.d/example.cnf)
file and recreate the MaxScale container to change the configuration.

To stop the containers, execute the following command. Optionally, use the -v
flag to also remove the volumes.

To run maxctrl in the container to see the status of the cluster:
```
$ docker-compose exec maxscale maxctrl list servers
┌─────────┬─────────┬──────┬─────────────┬─────────────────┬──────────┐
│ Server  │ Address │ Port │ Connections │ State           │ GTID     │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────────┤
│ server1 │ master  │ 3306 │ 0           │ Master, Running │ 0-3000-5 │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────────┤
│ server2 │ slave1  │ 3306 │ 0           │ Slave, Running  │ 0-3000-5 │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────────┤
│ server3 │ slave2  │ 3306 │ 0           │ Running         │ 0-3000-5 │
└─────────┴─────────┴──────┴─────────────┴─────────────────┴──────────┘

```

The cluster is configured to utilize automatic failover. To illustrate this you can stop the master
container and watch for maxscale to failover to one of the original slaves and then show it rejoining
after recovery:
```
$ docker-compose stop master
Stopping maxscaledocker_master_1 ... done
$ docker-compose exec maxscale maxctrl list servers
┌─────────┬─────────┬──────┬─────────────┬─────────────────┬─────────────┐
│ Server  │ Address │ Port │ Connections │ State           │ GTID        │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼─────────────┤
│ server1 │ master  │ 3306 │ 0           │ Down            │ 0-3000-5    │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼─────────────┤
│ server2 │ slave1  │ 3306 │ 0           │ Master, Running │ 0-3001-7127 │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼─────────────┤
│ server3 │ slave2  │ 3306 │ 0           │ Slave, Running  │ 0-3001-7127 │
└─────────┴─────────┴──────┴─────────────┴─────────────────┴─────────────┘
$ docker-compose start master
Starting master ... done
$ docker-compose exec maxscale maxctrl list servers
┌─────────┬─────────┬──────┬─────────────┬─────────────────┬─────────────┐
│ Server  │ Address │ Port │ Connections │ State           │ GTID        │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼─────────────┤
│ server1 │ master  │ 3306 │ 0           │ Slave, Running  │ 0-3001-7127 │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼─────────────┤
│ server2 │ slave1  │ 3306 │ 0           │ Master, Running │ 0-3001-7127 │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼─────────────┤
│ server3 │ slave2  │ 3306 │ 0           │ Slave, Running  │ 0-3001-7127 │
└─────────┴─────────┴──────┴─────────────┴─────────────────┴─────────────┘

```

Once complete, to remove the cluster and maxscale containers:

```
docker-compose down -v
```

## Documentation

### Sources
- Zak Rubin
  - [MaxScale Docker on GitHub](https://github.com/Zohan/maxscale-docker)
- Christine Sutton
  - [Panopto Video](https://rtc.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=9c492e9a-b3d1-46be-a657-b1870016c05a&autoplay=False&interactivity=all&start=0&showtitle=True&offerviewer=True&captions=False&showbrand=True&ltiCourseID=Canvas%5c2471314&isLTIEmbed=true&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InhYTGt6ejUybGNhWGhZWjR2QVl1bXRYNmQxdyIsImtpZCI6InhYTGt6ejUybGNhWGhZWjR2QVl1bXRYNmQxdyJ9.eyJpc3MiOiJodHRwczovL3J0Yy5ob3N0ZWQucGFub3B0by5jb20vUGFub3B0by9vYXV0aDIiLCJhdWQiOiJodHRwczovL3J0Yy5ob3N0ZWQucGFub3B0by5jb20vUGFub3B0by9vYXV0aDIvcmVzb3VyY2VzIiwiZXhwIjoxNzE3NzA0NzQ5LCJuYmYiOjE3MTc3MDQ2ODksImNsaWVudF9pZCI6ImMzMTNkZWEzLWIyZjgtNDFlNi05NDQwLWFkNDEwMDYzYTY3YSIsInNjb3BlIjoidmlld0VtYmVkZGVkQ29udGVudCIsInN1YiI6IjFkNzcxZDVmLTk3NmUtNGQxNi1hODQ3LWIwMzYwMTg3MWViOSIsImF1dGhfdGltZSI6MTcxNzcwNDY4OSwiaWRwIjoiaWRzcnYiLCJyb2xlIjoidmlld2VyIiwic2Vzc2lvbl9pZCI6IjAyNWQxYTgwLTMxNmQtNGM2My05ZWUyLWIxODcwMTRjYmVmOCIsIm5hbWUiOiJUeWxlciBTYWJpbiIsImFtciI6WyJwYXNzd29yZCJdfQ.WYxgpGloOELWWtW1i_YdYv1R4VAyM1gNNU2_QYXRY-En8ODLQZH76vl_GBaPMBmmLWLyj7ND7RYLZKIZG-uRYsOrMS8OMVgh9zqxN_maZE_KdZpEzgdvBH5tM_NLv17EMzDKWHzGcj1lKrTtYmR1NitumC6Lehub1Bfda5-SwTNHZNT8T0mJGNat5-2W85o1IBLC-uRm5URhYoIET1uI7B0QdEL6wpl4XJ2MlQbUEzJTQiGSQ8pGuWZEXQt6VNbTs-rsbVQhVFSOMa4Slyukr1FvuDOeVrXfAJuGb9B6INpcSpvK30quVbKD0GBtpEiNGDTLvBwOiZRwAquOnE651A#access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InhYTGt6ejUybGNhWGhZWjR2QVl1bXRYNmQxdyIsImtpZCI6InhYTGt6ejUybGNhWGhZWjR2QVl1bXRYNmQxdyJ9.eyJpc3MiOiJodHRwczovL3J0Yy5ob3N0ZWQucGFub3B0by5jb20vUGFub3B0by9vYXV0aDIiLCJhdWQiOiJodHRwczovL3J0Yy5ob3N0ZWQucGFub3B0by5jb20vUGFub3B0by9vYXV0aDIvcmVzb3VyY2VzIiwiZXhwIjoxNzE3NzA4Mjg5LCJuYmYiOjE3MTc3MDQ2ODksImNsaWVudF9pZCI6ImMzMTNkZWEzLWIyZjgtNDFlNi05NDQwLWFkNDEwMDYzYTY3YSIsInNjb3BlIjpbImFwaSIsIm9mZmxpbmVfYWNjZXNzIiwidmlld0VtYmVkZGVkQ29udGVudCJdLCJzdWIiOiIxZDc3MWQ1Zi05NzZlLTRkMTYtYTg0Ny1iMDM2MDE4NzFlYjkiLCJhdXRoX3RpbWUiOjE3MTc3MDQ2ODksImlkcCI6Imlkc3J2Iiwicm9sZSI6InZpZXdlciIsInNlc3Npb25faWQiOiIwMjVkMWE4MC0zMTZkLTRjNjMtOWVlMi1iMTg3MDE0Y2JlZjgiLCJuYW1lIjoiVHlsZXIgU2FiaW4iLCJhbXIiOlsicGFzc3dvcmQiXX0.TpABFkJuLLlzFYbIt7KA-oWO5-3DfnytrX0mYPbQxFNMoh56OAGk3grddJtmdg9RJAYHbyd2sa9NOODON8ij7uQTdHe_hb2EVIzxAUlSpQX8M9CgqkrHaxp1NTTDYLKoTv0ZwO7_1pUONsFppy8BI6mO89ZbD2_OAi59518KpTypvlW-aaWNAVPDGbKeKrQVayI2Es-gacDl1jJJFZScP4wqShITZoGzUFel3eBv0faEiWbXAH9-8A8ccHhMuu-yrYdrTPGAankUTwTFaiFVoDPr6K_1zTffMhkhWBmMC8HyBFrF-2BeunUuIaTENA1n2VNUCcWVK9az2QNpxhqT_w)
- Brian Huang
- Matt Bennett
- [List of ANSI color escape sequences on Stack Overflow](https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences)
- [ASCII Art in Python on Stack Overflow](https://stackoverflow.com/questions/13076194/ascii-art-in-python)
- [Simple Sharding Tutorial on GitHub](https://github.com/mariadb-corporation/MaxScale/blob/2.3/Documentation/Tutorials/Simple-Sharding-Tutorial.md)
- [Documentation Contents on GitHub](https://github.com/mariadb-corporation/MaxScale/blob/2.3/Documentation/Documentation-Contents.md)
- [Configuration Guide on GitHub](https://github.com/mariadb-corporation/MaxScale/blob/2.3/Documentation/Getting-Started/Configuration-Guide.md)
- [MaxAdmin Reference on GitHub](https://github.com/mariadb-corporation/MaxScale/blob/2.3/Documentation/Reference/MaxAdmin.md)
- [MariaDB MaxScale 2.5 Simple Sharding with Two Servers](https://mariadb.com/kb/en/mariadb-maxscale-25-simple-sharding-with-two-servers/)
- [MaxScale Docker on GitHub](https://github.com/Zohan/maxscale-docker)
- [GitHub Basic Writing and Formatting Syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
