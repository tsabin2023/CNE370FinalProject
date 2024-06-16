## Table of Contents

[Introduction](https://github.com/tsabin2023/CNE370FinalProject?tab=readme-ov-file#introduction)

[Running](https://github.com/tsabin2023/CNE370FinalProject?tab=readme-ov-file#running)

[Maxscale Docker-Compose Setup](https://github.com/tsabin2023/CNE370FinalProject?tab=readme-ov-file#maxscale-docker-compose-setup)

[Configuration](https://github.com/tsabin2023/CNE370FinalProject?tab=readme-ov-file#configuration)

[Testing Sharded Database Configuration with Python Script](https://github.com/tsabin2023/CNE370FinalProject?tab=readme-ov-file#testing-sharded-database-configuration-with-python-script)

[Documentation](https://github.com/tsabin2023/CNE370FinalProject?tab=readme-ov-file#documentation)

## Introduction

The goal of this project is to use sharding database architecture to split a database into smaller, more manageable pieces called shards, allowing for horizontal scaling for improved performance because no single server handles all the requests. The following technologies are used

 - Docker is for running applications inside containers, allowing for consistent environments across multiple stages of development and deployment

 - Docker Compose runs multi-container Docker applications

 - MaxScale is an advanced database proxy for MariaDB and MySQL databases

This project was forked from Zak Rubin's Maxscale Docker Project [Zohan MaxScale Docker Project](https://github.com/Zohan/maxscale-docker) and originally was set up with
 - master slave setup, 4 containers
 - non sharded

I have alterered it to use

 - 3 containers, sharded with 2 sharded databases with data
 - In addition I added a python script to demo query execution of sharded architecture

## Running
Prereqs:

On the host machine:
- Python 3 IDE
	- packages: mysql-connector
 
On the server machine:
- Ubuntu 22.04 server
- [Docker](https://docs.docker.com/engine/install/ubuntu/), [Docker-Compose](https://docs.docker.com/compose/install/)

## Maxscale Docker-Compose Setup
**The following steps will be performed on the server**

If you do not have Git, install git through the following command otherwise move onto the next step
```
sudo apt-get install git
```

Clone the project directory onto your server with the following command
```
git clone https://github.com/tsabin2023/CNE370FinalProject
```

Change into maxscale directory within the project repo directory
```
cd ./CNE370FinalProject/maxscale
```

Start the Docker containers with the following command, this will bring up our proxy and database servers
```
docker-compose build
docker-compose up -d
```

#### Optional Testing Section
***
After the MaxScale proxy and the database servers have started (takes a few minutes), we can test our databases manually by connecting to the proxy and performing queies/actions which uses the read (4008) write (4006) ports with the account **maxuser** as the username and **maxpwd** as the password

Enter the following command in the current directory to begin testing the databases, it will connect to the proxy, allowing you to execute SQL queries
```
mariadb -umaxuser -pmaxpwd -h 127.0.0.1 -P 4000
```

Below is an example of the output of the command
```
Welcome to the MariaDB monitor.  Commands end with ; or \g.

Your MariaDB connection id is 164

Server version: 10.3.39-MariaDB-1:10.3.39+maria~ubu2004-log mariadb.org binary distribution
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 
```

Close the connection with the following command
```
exit
```
***

Checking the status of the databases
```
docker-compose exec maxscale maxctrl list servers
```

Below is an example of the output of the command
```
┌─────────┬──────────┬──────┬─────────────┬─────────────────┬──────┬─────────────────┐

│ Server  │ Address  │ Port │ Connections │ State           │ GTID │ Monitor         │

├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────┼─────────────────┤

│ server1 │ primary1 │ 3306 │ 0           │ Master, Running │      │ MariaDB-Monitor │

├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────┼─────────────────┤

│ server2 │ primary2 │ 3306 │ 0           │ Running         │      │ MariaDB-Monitor │

└─────────┴──────────┴──────┴─────────────┴─────────────────┴──────┴─────────────────┘
```

Remove the Docker containers with the following command
```
docker-compose down -v
```

## Configuration

The original file that this project is forked from, contains MaxScale configured with a three node master-slave cluster. It has now been modified to use a proxy with sharded configuration between two databases

The first thing I did was rename the sql sub-folders in the sql folder to primary 1 and primary 2, to represent the change in architecture.

Then I download the provided shard 1 and shard 2 files that were provided and shard 1 in primary 1 and shard 2 in primary 2. This meant the databases have persistent data because I configured volumes of database container

Next I went into the docker-compose.yml in the maxscale folder and modified its contents to follow a sharded architucture. 
This meant changing the services of master and slave names to primary1 and primary2, and also in the volumes so that I could access the shards 1 and 2 that I had already put in their respective folders

This also meant I had to change the depends_on to the same names as the services have and setting ip a shard listener on port 4000, that way I have a proxy to run quearies through without querying the databases directly. Note shard archture needs a listening port for the proxy and the default port is 4000. 

```
 maxscale:
        image: mariadb/maxscale:latest
        depends_on:
            - primary1
            - primary2
        volumes:
            - ./maxscale.cnf.d:/etc/maxscale.cnf.d
        ports:
            - "4000:4000"  # shard listener
            - "4006:4006"  # readwrite port
            - "4008:4008"  # readonly port
            - "8989:8989"  # REST API port
```

There needed to be changes to the example.cnf in the sub-folder maxscale.cnf.d which is in the maxscale folder
Names of master was changed to primary1 and slave1 to primary 2, slave2 was no longer need, so I removed it.
The next step was to create the shard architectue by adding a Sharded Service and a Sharded Service Listener and set that to port 4000 to proxy queries to the sharded databases, see code below 

```
[Sharded-Service]
type=service
router=schemarouter
servers=server1,server2
user=maxuser
password=maxpwd

[Sharded-Service-Listener]
type=listener
service=Sharded-Service
protocol=MariaDBClient
port=4000
```

After that, I got rid of server 3 on the MariaDB-Monitor, as it was no-longer needed.
This process of removeing server 3 was repreated for the Read-Only-Service and Read-Write-Service.
No other changes to this file were required.

Furthermore, I added a python file in the projects folder for testing the shard architecture using sql queries. 

## Testing Sharded Database Configuration with Python Script
**The following steps will be performed on the server**

Getting the ip address of the server

Open the terminal and enter the following command to display the ip address
```
ifconfig
```

Write down the ip address of the server

**The following steps will be performed on the host machine**

To run the python file open your IDE that runs Python 3, this will vary from user to user

Option 1 Use the Version Control System (VCS) on you IDE and find the clone the repo https://github.com/tsabin2023/CNE370FinalProject
this will differ depending on what IDE you have installed.

Option 2. If you do not have Git installed, install Git for your host OS's IDE. Once installed, clone from the IDE terminal with the following command
```
git clone https://github.com/tsabin2023/CNE370FinalProject
```

Option 3. Create a new file (you may have to create a new project first) in your IDE and name it CNE370Final.py
Then copy and paste the contents of CNE370Final.py from the repo https://github.com/tsabin2023/CNE370FinalProject
and paste the contents into the python file you just made

In your IDE configure your Python Interpreter to be 3.11, how to do this will vary based on the IDE
Also, in your IDE's virtual enviroment for the python file, install the package mysql-connector. How to do this will vary based on your IDE

In the python file CNE370Final.py look for the line with the # replace '10.0.0.28'  with your server's ip address, eg. 'ipaddress' and put in the ipadress from the server that you wrote down

Run the python file, how this is done may vary depending on the IDE you are using

The first query and the first 15 results of query 2 is from the terminal output, and it will look like this
```
*******************************************
* 1. The largest zipcode in zipcodes_one: *
*******************************************

(47750,)

**********************************************
* 2. All zipcodes where state=KY (Kentucky): *
**********************************************

41503 42201 42202 42120 40801 42602 41601 42204 42020 42603 42122 40402 41121 40902 42021
...
```

If you want to see the full terminal output, click on the link
[View terminal.txt](https://github.com/tsabin2023/CNE370FinalProject/blob/master/terminal.txt)

## Documentation

### Sources
- Zak Rubin
  - [MaxScale Docker on GitHub](https://github.com/Zohan/maxscale-docker)
- Christine Sutton
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
- [https://github.com/mariadb-corporation/maxscale-docker/blob/master/README.md](https://github.com/mariadb-corporation/maxscale-docker/blob/master/README.md)
- [Get Started with MariaDB Using Docker in 3 Steps](https://mariadb.com/resources/blog/get-started-with-mariadb-using-docker-in-3-steps/)
- [MariaDB on Docker Hub](https://hub.docker.com/_/mariadb)

[⬆️Back to Table of Contents](https://github.com/tsabin2023/CNE370FinalProject?tab=readme-ov-file#table-of-contents)
