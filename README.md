Introduction (What does this do?)



Follows good documentation principles: Headers, Sections, Links, Code blocks, etc. (2 Points)

# Introduction to Database Shard Github

This Docker image runs the 2.4 version of MariaDB MaxScale image: mariadb:10.3, modified into shard architecture with two sharded database.

-	[Travis CI:  
	![build status badge](https://img.shields.io/travis/mariadb-corporation/maxscale-docker/master.svg)](https://travis-ci.org/mariadb-corporation/maxscale-docker/
branches)

- Zak Rubin
  - [MaxScale Docker on GitHub](https://github.com/Zohan/maxscale-docker)

## Running
note the following assumptions are made, you have a machine with a python 3 IDE installed, you know how to pick your IDE python 3 interpreter and install packages in its enviroment, and you have a server with Ubuntu 22.04, know how to access its terminal, and already have Docker and Docker-Compose and installed. https://docs.docker.com/engine/install/ubuntu/
https://docs.docker.com/compose/install/

Step 1.
from your server terminal type/copy and paste

```
git clone https://github.com/tsabin2023/CNE370FinalProject
```
Press enter

if you have issues make sure Git is installed on your machine

```
sudo apt-get install git
```
Press enter

Step 2.

[The MaxScale docker-compose setup](./docker-compose.yml) 

```
cd ./CNE370FinalProject/maxscale
```

contains MaxScale
configured with a three node sharded databse. To start it, run the
following commands in this directory.

```
docker-compose build
docker-compose up -d
```
 Note this may take some time, be patient.

check to see if the containers are up and running
```
docker ps -a
```

Here's an example of what it should look similar to

```
CONTAINER ID   IMAGE                     COMMAND                  CREATED          STATUS          PORTS                                                                                                                                                                                  NAMES
3ab460c0054d   mariadb/maxscale:latest   "/usr/bin/tini -- do…"   11 minutes ago   Up 10 minutes   0.0.0.0:4000->4000/tcp, :::4000->4000/tcp, 0.0.0.0:4006->4006/tcp, :::4006->4006/tcp, 0.0.0.0:4008->4008/tcp, :::4008->4008/tcp, 3306/tcp, 0.0.0.0:8989->8989/tcp, :::8989->8989/tcp   maxscale_maxscale_1
caec9b432531   mariadb:10.3              "docker-entrypoint.s…"   11 minutes ago   Up 11 minutes   0.0.0.0:4002->3306/tcp, :::4002->3306/tcp                                                                                                                                              maxscale_primary2_1
9e6537d04d66   mariadb:10.3              "docker-entrypoint.s…"   11 minutes ago   Up 11 minutes   0.0.0.0:4001->3306/tcp, :::4001->3306/tcp                                                                                                                                              maxscale_primary1_1
```


## Configuration

origional vs. current

how I modified the file configuration

Hi level view with some key code. What you canged and why

## Maxscale Docker-Compose Setup


## Testing

Step 3.

On you servers terminal, type
```
ifconfig
```
Write down the ipaddress of the server

To run the python file and see the query results, on you machine, not the server in the previous steps,

Go into you IDE that runs Python 3, this will very from user to user.

Option 1 Is to use the vcs on you IDE and find the clone the repo https://github.com/tsabin2023/CNE370FinalProject
this will differ depending on what IDE you have installed.

Option 2. Is to try and clone from the IDE terminal, this may vary depending on the IDE, but try

```
git clone https://github.com/tsabin2023/CNE370FinalProject
```
Press enter

if you have issues make sure Git is installed on your machine

```
sudo apt-get install git
```

Option 3. Create a new file (you may have to create a new project first) in your IDE and name it CNE370Final.py
Then copy and paste the contents of CNE370Final.py from the repo https://github.com/tsabin2023/CNE370FinalProject
and paste the contents into the python file you just made.

In your IDE configure your Python Interpreter to be 3.11, how to do this will vary based on the IDE.
Also, in your IDE's virtual enviroment for the python file, install package mysql-connector. How to do this will vary based on IDE and you may need to install additional packages like PyMySQL, mysql-connector-python-rf, etc. 

Step 4. In the python file CNE370Final.py look for the line with the # replace '10.0.0.28'  with your server's ip address, eg. 'ipaddress' and put in the ipadress from the server that you wrote down.

Run the python file, how this is done may vary depending on the IDE you are using. 

You will see the output in the terminal and it will look like this. 

```
*******************************************
* 1. The largest zipcode in zipcodes_one: *
*******************************************

(47750,)

**********************************************
* 2. All zipcodes where state=KY (Kentucky): *
**********************************************

(41503,)
(42201,)
(42202,)
(42120,)
(40801,)
(42602,)
(41601,)
(42204,)
(42020,)
(42603,)
(42122,)
(40402,)
(41121,)
(40902,)
(42021,)
(40903,)
(41712,)
(41512,)
(40803,)
(41101,)
(41102,)
(41105,)
(41114,)
(42206,)
(42123,)
(41602,)
(41713,)
(40003,)
(42022,)
(41603,)
(40906,)
(40946,)
(40004,)
(42023,)
(42024,)
(42402,)
(40104,)
(40806,)
(41714,)
(41311,)
(41203,)
(41604,)
(42320,)
(40006,)
(42322,)
(42323,)
(42324,)
(42207,)
(41513,)
(41514,)
(41535,)
(41567,)
(40807,)
(42025,)
(40403,)
(40404,)
(42516,)
(40007,)
(41605,)
(40913,)
(41606,)
(42712,)
(40914,)
(40405,)
(40808,)
(40915,)
(41804,)
(41832,)
(41124,)
(41160,)
(41226,)
(40810,)
(40816,)
(40008,)
(41607,)
(42027,)
(42713,)
(41719,)
(41314,)
(41351,)
(41364,)
(41204,)
(40107,)
(42101,)
(42102,)
(42103,)
(42104,)
(42128,)
(40009,)
(40108,)
(42715,)
(42741,)
(42325,)
(40409,)
(42518,)
(40109,)
(42210,)
(40921,)
(40410,)
(41721,)
(40010,)
(42716,)
(41722,)
(41517,)
(40310,)
(42717,)
(42028,)
(42519,)
(42211,)
(42327,)
(42371,)
(42029,)
(40813,)
(40011,)
(40075,)
(42718,)
(42719,)
(42733,)
(40376,)
(41301,)
(41360,)
(41519,)
(42720,)
(42721,)
(42722,)
(41408,)
(40923,)
(40311,)
(40350,)
(41725,)
(41128,)
(41129,)
(42127,)
(40815,)
(42724,)
(42214,)
(42328,)
(42330,)
(42215,)
(40012,)
(41727,)
(42726,)
(42404,)
(40312,)
(41317,)
(40313,)
(42332,)
(40110,)
(42216,)
(42031,)
(40927,)
(40111,)
(40819,)
(42728,)
(42753,)
(42032,)
(41729,)
(40701,)
(40702,)
(41731,)
(41819,)
(42406,)
(40013,)
(40419,)
(40820,)
(42033,)
(40014,)
(41413,)
(42217,)
(41810,)
(42333,)
(42729,)
(40823,)
(42035,)
(40115,)
(41615,)
(40422,)
(40423,)
(40452,)
(41616,)
(42408,)
(40824,)
(41812,)
(41735,)
(40316,)
(40930,)
(42036,)
(41736,)
(42409,)
(41520,)
(42321,)
(42326,)
(42337,)
(42731,)
(42219,)
(42338,)
(42339,)
(42528,)
(41621,)
(41739,)
(42037,)
(42410,)
(40729,)
(41622,)
(42732,)
(40018,)
(42038,)
(42129,)
(40117,)
(42701,)
(42702,)
(41522,)
(41542,)
(42220,)
(42280,)
(40317,)
(40019,)
(40730,)
(41740,)
(40826,)
(41815,)
(40827,)
(42567,)
(40828,)
(40843,)
(41425,)
(40118,)
(40020,)
(42221,)
(41426,)
(40932,)
(40119,)
(42039,)
(40319,)
(42040,)
(41524,)
(42533,)
(40022,)
(40023,)
(41743,)
(41219,)
(40935,)
(40997,)
(41139,)
(41526,)
(42343,)
(42361,)
(41527,)
(42223,)
(40121,)
(40122,)
(42133,)
(40939,)
(40940,)
(40601,)
(40602,)
(40603,)
(40604,)
(40618,)
(40619,)
(40620,)
(40621,)
(40622,)
(42134,)
(42135,)
(42411,)
(41528,)
(40322,)
(42041,)
(42140,)
(40140,)
(41817,)
(40941,)
(41630,)
(41632,)
(41141,)
(41745,)
(40324,)
(42044,)
(40943,)
(42131,)
(42141,)
(42142,)
(42156,)
(42740,)
(40025,)
(40944,)
(40026,)
(42232,)
(42742,)
(42344,)
(41142,)
(42045,)
(40328,)
(40734,)
(40434,)
(40829,)
(41143,)
(42743,)
(41144,)
(42345,)
(41631,)
(40142,)
(42234,)
(41222,)
(41821,)
(42047,)
(42413,)
(41746,)
(41747,)
(42048,)
(40143,)
(40171,)
(41531,)
(42746,)
(40818,)
(40831,)
(40840,)
(40858,)
(40144,)
(40178,)
(41635,)
(40330,)
(40027,)
(42347,)
(42348,)
(42364,)
(41701,)
(41702,)
(41723,)
(42049,)
(41332,)
(41333,)
(40949,)
(41534,)
(42419,)
(42420,)
(42236,)
(42050,)
(42051,)
(41636,)
(40951,)
(41822,)
(40953,)
(42152,)
(41132,)
(41146,)
(42748,)
(42153,)
(42240,)
(42241,)
(42349,)
(42749,)
(40844,)
(40145,)
(41640,)
(40845,)
(40437,)
(41749,)
(41762,)
(41766,)
(41214,)
(41224,)
(40955,)
(40336,)
(40472,)
(40146,)
(42350,)
(41338,)
(41824,)
(41149,)
(41642,)
(41825,)
(41307,)
(41310,)
(41339,)
(41366,)
(41390,)
(42629,)
(41751,)
(41774,)
(40337,)
(41537,)
(41563,)
(41826,)
(42252,)
(41538,)
(40440,)
(40737,)
(40339,)
(40847,)
(40958,)
(42053,)
(41539,)
(40442,)
(42054,)
(41828,)
(41859,)
(42154,)
(41754,)
(42055,)
(42056,)
(41643,)
(42254,)
(40031,)
(40032,)
(40444,)
(40446,)
(40342,)
(40033,)
(40150,)
(41831,)
(42058,)
(42754,)
(42755,)
(40849,)
(42256,)
(42351,)
(40502,)
(40503,)
(40504,)
(40505,)
(40506,)
(40507,)
(40508,)
(40509,)
(40510,)
(40511,)
(40512,)
(40513,)
(40514,)
(40515,)
(40516,)
(40517,)
(40522,)
(40523,)
(40524,)
(40526,)
(40533,)
(40536,)
(40544,)
(40546,)
(40550,)
(40555,)
(40574,)
(40575,)
(40576,)
(40577,)
(40578,)
(40579,)
(40580,)
(40581,)
(40582,)
(40583,)
(40588,)
(40591,)
(40598,)
(42539,)
(41540,)
(40740,)
(41834,)
(42352,)
(40445,)
(40460,)
(40724,)
(40741,)
(40742,)
(40743,)
(40744,)
(40745,)
(41347,)
(40037,)
(41348,)
(41201,)
(41230,)
(40201,)
(40202,)
(40203,)
(40204,)
(40205,)
(40206,)
(40207,)
(40208,)
(40209,)
(40210,)
(40211,)
(40212,)
(40213,)
(40214,)
(40215,)
(40216,)
(40217,)
(40218,)
(40219,)
(40220,)
(40221,)
(40222,)
(40223,)
(40224,)
(40225,)
(40228,)
(40229,)
(40231,)
(40232,)
(40233,)
(40241,)
(40242,)
(40243,)
(40245,)
(40250,)
(40251,)
(40252,)
(40253,)
(40255,)
(40256,)
(40257,)
(40258,)
(40259,)
(40261,)
(40266,)
(40268,)
(40269,)
(40270,)
(40272,)
(40280,)
(40281,)
(40282,)
(40283,)
(40285,)
(40287,)
(40289,)
(40290,)
(40291,)
(40292,)
(40293,)
(40294,)
(40295,)
(40296,)
(40297,)
(40298,)
(40299,)
(40129,)
(42060,)
(41231,)
(42061,)
(41232,)
(40854,)
(40855,)
(42063,)
(41543,)
(41544,)
(41558,)
(40152,)
(41647,)
(42354,)
(40447,)
(40488,)
(40448,)
(40153,)
(41835,)
(42355,)
(40040,)
(42431,)
(42757,)
(41547,)
(41836,)
(41451,)
(42259,)
(40962,)
(42436,)
(42758,)
(42064,)
(42759,)
(42631,)
(41159,)
(41649,)
(40830,)
(40964,)
(40041,)
(42066,)
(41837,)
(41838,)
(41855,)
(41234,)
(40334,)
(40346,)
(42069,)
(41612,)
(41650,)
(42541,)
(40965,)
(40347,)
(42070,)
(40348,)
(42762,)
(40045,)
(41651,)
(40856,)
(41352,)
(42633,)
(40351,)
(42437,)
(42261,)
(42440,)
(40046,)
(42157,)
(42764,)
(40353,)
(40456,)
(40473,)
(40047,)
(41839,)
(41548,)
(40155,)
(42765,)
(42071,)
(41549,)
(42544,)
(40048,)
(41840,)
(40049,)
(40050,)
(42076,)
(40051,)
(40052,)
(40355,)
(40340,)
(40356,)
(40357,)
(42442,)
(42262,)
(42159,)
(41238,)
(41164,)
(42265,)
(40358,)
(40972,)
(40981,)
(41459,)
(42301,)
(42302,)
(42303,)
(42304,)
(42334,)
(42356,)
(40359,)
(40360,)
(40366,)
(42001,)
(42002,)
(42003,)
(40461,)
(41216,)
(41240,)
(41257,)
(40361,)
(40362,)
(42160,)
(42634,)
(40464,)
(40862,)
(40863,)
(40157,)
(42266,)
(40055,)
(40363,)
(40468,)
(40056,)
(41553,)
(42366,)
(41554,)
(41501,)
(41502,)
(41571,)
(41250,)
(42635,)
(41843,)
(40977,)
(41555,)
(41844,)
(41861,)
(40755,)
(40036,)
(40057,)
(42444,)
(40058,)
(42367,)
(41845,)
(41645,)
(41653,)
(41362,)
(42445,)
(41619,)
(41655,)
(40059,)
(42441,)
(42450,)
(40865,)
(41166,)
(41557,)
(40159,)
(40160,)
(40060,)
(41847,)
(42451,)
(41559,)
(42638,)
(42368,)
(40161,)
(40475,)
(40476,)
(40162,)
(41254,)
(40979,)
(42452,)
(41560,)
(42273,)
(42274,)
(40759,)
(41561,)
(42369,)
(42163,)
(41365,)
(42370,)
(42275,)
(41367,)
(41848,)
(41464,)
(41168,)
(41169,)
(42642,)
(42276,)
(42372,)
(40370,)
(40061,)
(42453,)
(40062,)
(41368,)
(40063,)
(42078,)
(40371,)
(40372,)
(41465,)
(40481,)
(41171,)
(41759,)
(40982,)
(42553,)
(42164,)
(42455,)
(41849,)
(42079,)
(40983,)
(40374,)
(41562,)
(40065,)
(40066,)
(40165,)
(41564,)
(40763,)
(40067,)
(42456,)
(41763,)
(41764,)
(40068,)
(42081,)
(42457,)
(42171,)
(41173,)
(42501,)
(42502,)
(42503,)
(42564,)
(42776,)
(42374,)
(41174,)
(41175,)
(42458,)
(40069,)
(41256,)
(40379,)
(40484,)
(40380,)
(41659,)
(42647,)
(41566,)
(40170,)
(40868,)
(40988,)
(41568,)
(42649,)
(42459,)
(42460,)
(40070,)
(42124,)
(42130,)
(42166,)
(42782,)
(42285,)
(42082,)
(42558,)
(40071,)
(41660,)
(41260,)
(42083,)
(41189,)
(42084,)
(41262,)
(42151,)
(42167,)
(41862,)
(40870,)
(41663,)
(42286,)
(40995,)
(41263,)
(40486,)
(41264,)
(42461,)
(42784,)
(42376,)
(41135,)
(41179,)
(41385,)
(41265,)
(40383,)
(40384,)
(41772,)
(41760,)
(41773,)
(41386,)
(40175,)
(41572,)
(40385,)
(40076,)
(40873,)
(40874,)
(41267,)
(42085,)
(42462,)
(41666,)
(40489,)
(41180,)
(40176,)
(41667,)
(40387,)
(41775,)
(41421,)
(41472,)
(41477,)
(42377,)
(42086,)
(40177,)
(40077,)
(41268,)
(42463,)
(41669,)
(42788,)
(42464,)
(41833,)
(41858,)
(42378,)
(42653,)
(42087,)
(40492,)
(41181,)
(40769,)
(41271,)
(40078,)
(40390,)
(40391,)
(40392,)
(42565,)
(42088,)
(41255,)
(41274,)
(40771,)
(42170,)
(42288,)
(41776,)
(41183,)
(41777,)
(41778,)
(42566,)
(41397,)
(41001,)
(41002,)
(41003,)
(41004,)
(41005,)
(41006,)
(41007,)
(41008,)
(41045,)
(41010,)
(41011,)
(41012,)
(41014,)
(41015,)
(41016,)
(41017,)
(41018,)
(41019,)
(41030,)
(41031,)
(41033,)
(41034,)
(41035,)
(41037,)
(41039,)
(41040,)
(41041,)
(41022,)
(41042,)
(41043,)
(41044,)
(41046,)
(41048,)
(41049,)
(41051,)
(41052,)
(41053,)
(41054,)
(41055,)
(41056,)
(41059,)
(41061,)
(41062,)
(41063,)
(41064,)
(41065,)
(41071,)
(41072,)
(41073,)
(41074,)
(41075,)
(41076,)
(41099,)
(41080,)
(41081,)
(41083,)
(41085,)
(41086,)
(41091,)
(41092,)
(41093,)
(41094,)
(41095,)
(41096,)
(41097,)
(41098,)

********************************************
* 3. All zipcodes between 40000 and 41000: *
********************************************

(40801,)
(40402,)
(40902,)
(40903,)
(40803,)
(40003,)
(40906,)
(40946,)
(40004,)
(40104,)
(40806,)
(40006,)
(40807,)
(40403,)
(40404,)
(40007,)
(40913,)
(40914,)
(40405,)
(40808,)
(40915,)
(40810,)
(40816,)
(40008,)
(40107,)
(40009,)
(40108,)
(40409,)
(40109,)
(40921,)
(40410,)
(40010,)
(40310,)
(40813,)
(40011,)
(40075,)
(40376,)
(40923,)
(40311,)
(40350,)
(40815,)
(40012,)
(40312,)
(40313,)
(40110,)
(40927,)
(40111,)
(40819,)
(40701,)
(40702,)
(40013,)
(40419,)
(40820,)
(40014,)
(40823,)
(40115,)
(40422,)
(40423,)
(40452,)
(40824,)
(40316,)
(40930,)
(40729,)
(40018,)
(40117,)
(40317,)
(40019,)
(40730,)
(40826,)
(40827,)
(40828,)
(40843,)
(40118,)
(40020,)
(40932,)
(40119,)
(40319,)
(40022,)
(40023,)
(40935,)
(40997,)
(40121,)
(40122,)
(40939,)
(40940,)
(40601,)
(40602,)
(40603,)
(40604,)
(40618,)
(40619,)
(40620,)
(40621,)
(40622,)
(40322,)
(40140,)
(40941,)
(40324,)
(40943,)
(40025,)
(40944,)
(40026,)
(40328,)
(40734,)
(40434,)
(40829,)
(40142,)
(40143,)
(40171,)
(40818,)
(40831,)
(40840,)
(40858,)
(40144,)
(40178,)
(40330,)
(40027,)
(40949,)
(40951,)
(40953,)
(40844,)
(40145,)
(40845,)
(40437,)
(40955,)
(40336,)
(40472,)
(40146,)
(40337,)
(40440,)
(40737,)
(40339,)
(40847,)
(40958,)
(40442,)
(40031,)
(40032,)
(40444,)
(40446,)
(40342,)
(40033,)
(40150,)
(40849,)
(40502,)
(40503,)
(40504,)
(40505,)
(40506,)
(40507,)
(40508,)
(40509,)
(40510,)
(40511,)
(40512,)
(40513,)
(40514,)
(40515,)
(40516,)
(40517,)
(40522,)
(40523,)
(40524,)
(40526,)
(40533,)
(40536,)
(40544,)
(40546,)
(40550,)
(40555,)
(40574,)
(40575,)
(40576,)
(40577,)
(40578,)
(40579,)
(40580,)
(40581,)
(40582,)
(40583,)
(40588,)
(40591,)
(40598,)
(40740,)
(40445,)
(40460,)
(40724,)
(40741,)
(40742,)
(40743,)
(40744,)
(40745,)
(40037,)
(40201,)
(40202,)
(40203,)
(40204,)
(40205,)
(40206,)
(40207,)
(40208,)
(40209,)
(40210,)
(40211,)
(40212,)
(40213,)
(40214,)
(40215,)
(40216,)
(40217,)
(40218,)
(40219,)
(40220,)
(40221,)
(40222,)
(40223,)
(40224,)
(40225,)
(40228,)
(40229,)
(40231,)
(40232,)
(40233,)
(40241,)
(40242,)
(40243,)
(40245,)
(40250,)
(40251,)
(40252,)
(40253,)
(40255,)
(40256,)
(40257,)
(40258,)
(40259,)
(40261,)
(40266,)
(40268,)
(40269,)
(40270,)
(40272,)
(40280,)
(40281,)
(40282,)
(40283,)
(40285,)
(40287,)
(40289,)
(40290,)
(40291,)
(40292,)
(40293,)
(40294,)
(40295,)
(40296,)
(40297,)
(40298,)
(40299,)
(40129,)
(40854,)
(40855,)
(40152,)
(40447,)
(40488,)
(40448,)
(40153,)
(40040,)
(40962,)
(40830,)
(40964,)
(40041,)
(40334,)
(40346,)
(40965,)
(40347,)
(40348,)
(40045,)
(40856,)
(40351,)
(40046,)
(40353,)
(40456,)
(40473,)
(40047,)
(40155,)
(40048,)
(40049,)
(40050,)
(40051,)
(40052,)
(40355,)
(40340,)
(40356,)
(40357,)
(40358,)
(40972,)
(40981,)
(40359,)
(40360,)
(40366,)
(40461,)
(40361,)
(40362,)
(40464,)
(40862,)
(40863,)
(40157,)
(40055,)
(40363,)
(40468,)
(40056,)
(40977,)
(40755,)
(40036,)
(40057,)
(40058,)
(40059,)
(40865,)
(40159,)
(40160,)
(40060,)
(40161,)
(40475,)
(40476,)
(40162,)
(40979,)
(40759,)
(40370,)
(40061,)
(40062,)
(40063,)
(40371,)
(40372,)
(40481,)
(40982,)
(40983,)
(40374,)
(40065,)
(40066,)
(40165,)
(40763,)
(40067,)
(40068,)
(40069,)
(40379,)
(40484,)
(40380,)
(40170,)
(40868,)
(40988,)
(40070,)
(40071,)
(40870,)
(40995,)
(40486,)
(40383,)
(40384,)
(40175,)
(40385,)
(40076,)
(40873,)
(40874,)
(40489,)
(40176,)
(40387,)
(40177,)
(40077,)
(40492,)
(40769,)
(40078,)
(40390,)
(40391,)
(40392,)
(40771,)

***********************************************************
* 4. The TotalWages column where state=PA (Pennsylvania): *
***********************************************************

('11966378',)
('62923182',)
('',)
('7908593',)
('',)
('8273435',)
('13678147',)
('57568042',)
('',)
('',)
('34233845',)
('565791203',)
('',)
('',)
('667346676',)
('',)
('428649297',)
('379642102',)
('4377418',)
('22945575',)
('',)
('',)
('166009726',)
('25192378',)
('',)
('244184876',)
('',)
('',)
('16182812',)
('',)
('',)
('24607804',)
('',)
('11909237',)
('',)
('14895510',)
('61800486',)
('36624538',)
('213188865',)
('',)
('',)
('81026002',)
('',)
('',)
('10154710',)
('304377640',)
('10079246',)
('456509722',)
('',)
('168742357',)
('31979307',)
('',)
('386411937',)
('276106055',)
('38542847',)
('',)
('',)
('54055867',)
('72863036',)
('21760172',)
('702813430',)
('',)
('',)
('6820827',)
('9178957',)
('152126652',)
('',)
('14257506',)
('',)
('103160487',)
('8458867',)
('24217568',)
('50763937',)
('',)
('',)
('',)
('',)
('',)
('18150795',)
('',)
('45363175',)
('81522664',)
('9628942',)
('235024794',)
('49171202',)
('',)
('17223899',)
('360232514',)
('',)
('',)
('8881334',)
('',)
('21360563',)
('71382491',)
('134596903',)
('',)
('',)
('104817969',)
('8039977',)
('',)
('14799596',)
('9607297',)
('26038890',)
('',)
('119652085',)
('679300710',)
('326248980',)
('',)
('',)
('68164900',)
('',)
('14149364',)
('25059741',)
('',)
('',)
('',)
('',)
('81232781',)
('995419238',)
('',)
('',)
('',)
('77738234',)
('331848277',)
('32074134',)
('',)
('',)
('35680938',)
('34972022',)
('',)
('38840454',)
('72939133',)
('10478536',)
('',)
('21108945',)
('',)
('150473679',)
('',)
('28061222',)
('',)
('',)
('190075811',)
('98985609',)
('305522245',)
('10685781',)
('24802356',)
('14051987',)
('109300519',)
('',)
('22994918',)
('7602362',)
('30026477',)
('40912775',)
('',)
('',)
('72530338',)
('171480223',)
('24321411',)
('72940339',)
('7205491',)
('',)
('48056115',)
('',)
('30312952',)
('24044651',)
('',)
('76463734',)
('9752220',)
('9576851',)
('15619983',)
('18268459',)
('25591398',)
('',)
('80049185',)
('41587350',)
('249710855',)
('',)
('34815855',)
('',)
('21221858',)
('',)
('959075460',)
('136968162',)
('18879107',)
('',)
('16726545',)
('6920750',)
('29266605',)
('24790133',)
('',)
('14430302',)
('70682657',)
('',)
('',)
('',)
('',)
('',)
('8965152',)
('',)
('',)
('',)
('67209884',)
('',)
('6782584',)
('',)
('15913676',)
('54998460',)
('',)
('29637638',)
('24872739',)
('29628186',)
('',)
('',)
('103123091',)
('',)
('',)
('97314701',)
('',)
('20066426',)
('',)
('',)
('',)
('6240800',)
('52534454',)
('26703071',)
('',)
('',)
('305445260',)
('',)
('11408177',)
('60786679',)
('200507856',)
('',)
('',)
('45402898',)
('12187008',)
('25939151',)
('11806289',)
('30503013',)
('31478474',)
('10398906',)
('41506939',)
('',)
('19345947',)
('8203344',)
('',)
('143457531',)
('157446144',)
('',)
('42409749',)
('121995765',)
('',)
('8827706',)
('39293086',)
('',)
('199624498',)
('12613874',)
('268573628',)
('6623753',)
('',)
('',)
('',)
('43956771',)
('59634218',)
('',)
('',)
('36593692',)
('6263221',)
('159742451',)
('103698176',)
('218911354',)
('378565032',)
('503060220',)
('91802592',)
('245323547',)
('496141340',)
('404957360',)
('176873435',)
('5581092',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('120748627',)
('100884098',)
('11902567',)
('253666320',)
('5524898',)
('33272489',)
('10290246',)
('15595292',)
('224913655',)
('12748914',)
('26225401',)
('32415557',)
('47242624',)
('33487974',)
('33919933',)
('144526193',)
('',)
('6936759',)
('',)
('12340123',)
('41214130',)
('',)
('',)
('116119780',)
('',)
('',)
('',)
('',)
('223674294',)
('30719888',)
('25941683',)
('155269888',)
('101665384',)
('14566067',)
('',)
('56922657',)
('',)
('',)
('38947354',)
('',)
('',)
('15744297',)
('',)
('39814617',)
('',)
('969927359',)
('',)
('',)
('135173296',)
('',)
('58133709',)
('12225657',)
('334172363',)
('48581695',)
('24223115',)
('6423884',)
('7831488',)
('',)
('12284456',)
('',)
('25396938',)
('1137493815',)
('',)
('',)
('224898894',)
('27383977',)
('220493838',)
('36157584',)
('25303235',)
('',)
('',)
('43089257',)
('',)
('101604490',)
('106858455',)
('47927695',)
('11622434',)
('15877185',)
('35699992',)
('',)
('',)
('5956835',)
('',)
('',)
('',)
('27720523',)
('10549476',)
('',)
('29865297',)
('7428897',)
('11862271',)
('',)
('',)
('11845072',)
('321191147',)
('39652241',)
('',)
('31057971',)
('',)
('102362812',)
('287639620',)
('51800786',)
('22048162',)
('22113384',)
('43087865',)
('',)
('87932376',)
('43247866',)
('',)
('76074724',)
('35257131',)
('190312384',)
('',)
('',)
('8637578',)
('',)
('',)
('36073205',)
('',)
('21533613',)
('163215885',)
('449426514',)
('',)
('8831345',)
('7596015',)
('60375505',)
('',)
('',)
('13924446',)
('989845440',)
('',)
('24205469',)
('',)
('',)
('',)
('17623120',)
('47319006',)
('310854761',)
('26405239',)
('9334643',)
('10137702',)
('',)
('49226282',)
('25365851',)
('130411837',)
('279136118',)
('401535755',)
('116713364',)
('',)
('75272423',)
('',)
('',)
('',)
('42558828',)
('',)
('84731476',)
('30824282',)
('9994883',)
('',)
('',)
('23284895',)
('',)
('50793872',)
('271748273',)
('54230617',)
('',)
('10739531',)
('',)
('',)
('',)
('',)
('60106355',)
('10830066',)
('',)
('',)
('7436684',)
('',)
('',)
('443926805',)
('14150189',)
('28883868',)
('',)
('171158509',)
('15366469',)
('17744615',)
('',)
('26639115',)
('33137755',)
('19133855',)
('248577001',)
('157194416',)
('36599333',)
('',)
('50797697',)
('29094375',)
('',)
('8718935',)
('',)
('7913826',)
('20386842',)
('',)
('',)
('12421191',)
('',)
('',)
('15755963',)
('31652242',)
('',)
('310043394',)
('',)
('',)
('67716820',)
('147982434',)
('215572736',)
('103717406',)
('',)
('97912264',)
('382529605',)
('',)
('11742668',)
('8389314',)
('',)
('18522753',)
('',)
('19810468',)
('28953012',)
('',)
('',)
('24186561',)
('18903775',)
('35406144',)
('10549141',)
('18894905',)
('473258383',)
('886090859',)
('',)
('71977988',)
('9495496',)
('50359199',)
('9068780',)
('20100487',)
('13056624',)
('384156517',)
('',)
('',)
('173318236',)
('',)
('74937421',)
('54190238',)
('15026813',)
('17877897',)
('12196151',)
('17560164',)
('',)
('',)
('35275292',)
('',)
('',)
('222129870',)
('93537303',)
('189128586',)
('',)
('',)
('',)
('51143664',)
('7363975',)
('',)
('15978356',)
('30698033',)
('237676324',)
('432267895',)
('8348893',)
('48783362',)
('189763654',)
('8426976',)
('59110954',)
('',)
('',)
('58761636',)
('',)
('190363919',)
('420872113',)
('80698761',)
('',)
('293461862',)
('',)
('',)
('11041345',)
('33026075',)
('',)
('25162548',)
('49252110',)
('11060895',)
('28249137',)
('',)
('654596170',)
('',)
('',)
('33025940',)
('',)
('30339417',)
('62896393',)
('78216341',)
('',)
('15653513',)
('',)
('25874806',)
('19897009',)
('208895655',)
('',)
('156976608',)
('',)
('',)
('',)
('236356113',)
('155332792',)
('',)
('10878666',)
('201018295',)
('',)
('10745619',)
('',)
('',)
('37308607',)
('',)
('20513607',)
('44165551',)
('48085159',)
('17738933',)
('16382959',)
('29121700',)
('36844192',)
('62183983',)
('30121289',)
('22420395',)
('',)
('115339961',)
('12249664',)
('330884386',)
('',)
('37641641',)
('584154297',)
('183829198',)
('385699116',)
('186786922',)
('106986982',)
('439445092',)
('466100637',)
('154902188',)
('186811770',)
('244559083',)
('306085041',)
('197908591',)
('407469245',)
('200318202',)
('203171183',)
('358015075',)
('459915508',)
('758873902',)
('286304907',)
('137501261',)
('369565219',)
('480326744',)
('148970937',)
('114859798',)
('129720383',)
('16570357',)
('234252470',)
('522340375',)
('576114520',)
('290976828',)
('5237990',)
('',)
('292790291',)
('46354945',)
('271505879',)
('634101610',)
('612338255',)
('1096698229',)
('703048749',)
('448633204',)
('',)
('833341611',)
('',)
('376622393',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('24248448',)
('9873123',)
('26719972',)
('',)
('',)
('26623158',)
('29815419',)
('103476872',)
('53544824',)
('55055583',)
('180578248',)
('164348250',)
('',)
('47013538',)
('29615802',)
('43008750',)
('',)
('',)
('181481699',)
('',)
('',)
('',)
('7259127',)
('10891969',)
('',)
('84177391',)
('',)
('13785087',)
('8316497',)
('',)
('82175103',)
('25078384',)
('12751769',)
('',)
('',)
('97289662',)
('9738436',)
('38516538',)
('8350676',)
('80862667',)
('7145875',)
('9473132',)
('135386399',)
('',)
('10363966',)
('14272081',)
('48754085',)
('',)
('',)
('15145552',)
('17777179',)
('13765781',)
('',)
('55710102',)
('',)
('31127569',)
('66393004',)
('11616543',)
('79422132',)
('',)
('',)
('228327216',)
('7269557',)
('',)
('',)
('21204666',)
('',)
('22071193',)
('78070746',)
('36665944',)
('175357687',)
('91184187',)
('34008591',)
('37730837',)
('28157673',)
('',)
('128711405',)
('21255225',)
('44443315',)
('29753331',)
('853507834',)
('',)
('157548215',)
('297587131',)
('120156946',)
('',)
('',)
('26857085',)
('51509818',)
('37418571',)
('49693506',)
('',)
('30975871',)
('14977538',)
('',)
('',)
('8834704',)
('9429672',)
('23862776',)
('',)
('159031754',)
('6298208',)
('55505446',)
('8077562',)
('86027106',)
('',)
('32633996',)
('26522991',)
('',)
('19011590',)
('231571403',)
('',)
('',)
('',)
('37160889',)
('',)
('',)
('',)
('',)
('23147094',)
('10528368',)
('24363246',)
('14038273',)
('8186186',)
('68815339',)
('61038218',)
('',)
('',)
('22916257',)
('',)
('7998565',)
('532986947',)
('5873461',)
('416259144',)
('8287845',)
('',)
('8221151',)
('35627406',)
('',)
('41447934',)
('10185876',)
('23326326',)
('',)
('',)
('31200790',)
('33870823',)
('26045994',)
('14378082',)
('12468545',)
('14919718',)
('154863822',)
('10275079',)
('',)
('27763143',)
('',)
('17122787',)
('',)
('',)
('',)
('30059572',)
('',)
('',)
('130859298',)
('',)
('16729040',)
('158901473',)
('41883271',)
('',)
('96708590',)
('',)
('7607813',)
('',)
('',)
('192317224',)
('',)
('103477153',)
('415780890',)
('',)
('14530894',)
('174906051',)
('',)
('34013004',)
('116409170',)
('',)
('14391386',)
('359436582',)
('15778467',)
('264955711',)
('7131437',)
('',)
('13639670',)
('48134730',)
('',)
('',)
('',)
('',)
('55276780',)
('280753949',)
('',)
('',)
('',)
('',)
('33638459',)
('813552741',)
('',)
('170790904',)
('48474630',)
('194122621',)
('',)
('21209662',)
('',)
('',)
('26936690',)
('28265536',)
('8264552',)
('10357036',)
('',)
('',)
('',)
('',)
('80650006',)
('',)
('14584056',)
('104475327',)
('9328968',)
('11484841',)
('18603885',)
('47261653',)
('',)
('900817306',)
('',)
('',)
('7867724',)
('9233283',)
('',)
('',)
('22281572',)
('',)
('51236509',)
('26440710',)
('',)
('',)
('162505971',)
('9398569',)
('',)
('11310551',)
('28038859',)
('',)
('46071424',)
('',)
('',)
('9930605',)
('40451572',)
('47100176',)
('11213673',)
('138222569',)
('77475984',)
('20947643',)
('49793941',)
('76678666',)
('108113378',)
('126939909',)
('5518469',)
('20693943',)
('458104408',)
('854962113',)
('1022096857',)
('14551764',)
('191506188',)
('223477277',)
('',)
('27225585',)
('',)
('',)
('26222668',)
('201182358',)
('',)
('',)
('132730734',)
('13419116',)
('',)
('',)
('',)
('',)
('99692528',)
('44858195',)
('96180696',)
('93722027',)
('21017511',)
('48150039',)
('23499694',)
('',)
('327200272',)
('',)
('37504004',)
('',)
('112610454',)
('37100795',)
('229161800',)
('',)
('',)
('31230308',)
('18346017',)
('15807231',)
('',)
('24924016',)
('65381517',)
('39349346',)
('12070062',)
('',)
('61058758',)
('23420908',)
('143910583',)
('',)
('275673072',)
('51249014',)
('556553699',)
('6695256',)
('800231941',)
('531471504',)
('524896657',)
('',)
('88766685',)
('16814130',)
('333547254',)
('11276680',)
('8176566',)
('84294093',)
('170667121',)
('411173922',)
('',)
('23234277',)
('7132125',)
('21661621',)
('135580893',)
('',)
('9387111',)
('7850411',)
('352772363',)
('33407100',)
('',)
('176760049',)
('',)
('53186760',)
('34532671',)
('',)
('25394174',)
('',)
('',)
('27472582',)
('',)
('172076333',)
('13215431',)
('',)
('',)
('',)
('',)
('723962713',)
('',)
('',)
('',)
('37934925',)
('54455420',)
('190743310',)
('568739391',)
('444507730',)
('',)
('',)
('163855686',)
('92126754',)
('',)
('275558937',)
('444156894',)
('476586178',)
('',)
('',)
('56914178',)
('533114516',)
('5076542',)
('28060728',)
('',)
('',)
('92871162',)
('296208412',)
('27447716',)
('',)
('96393513',)
('32488684',)
('369984822',)
('149243842',)
('12536894',)
('',)
('84422963',)
('18037224',)
('',)
('75765854',)
('26816923',)
('',)
('',)
('304263573',)
('',)
('199251767',)
('28278937',)
('125431491',)
('14151028',)
('62750170',)
('378524991',)
('',)
('92102623',)
('',)
('15577877',)
('107919621',)
('277950639',)
('',)
('384630908',)
('',)
('145024379',)
('17501492',)
('',)
('369234015',)
('',)
('16401406',)
('182658973',)
('',)
('',)
('164081522',)
('',)
('29694546',)
('',)
('',)
('166843100',)
('80858410',)
('119132490',)
('413535355',)
('650918721',)
('',)
('6285322',)
('634507956',)
('92006370',)
('8444387',)
('',)
('471822317',)
('307938384',)
('',)
('12423211',)
('',)
('152103068',)
('551693191',)
('54799421',)
('21605125',)
('32568610',)
('',)
('',)
('144896708',)
('82828933',)
('7901178',)
('409937067',)
('',)
('',)
('368775495',)
('520261883',)
('',)
('13709056',)
('245601329',)
('69764541',)
('163083208',)
('31230980',)
('8996933',)
('47741375',)
('163923477',)
('120508500',)
('',)
('313542785',)
('118667283',)
('69221790',)
('',)
('13752227',)
('7343275',)
('27526500',)
('75908353',)
('',)
('',)
('',)
('61849964',)
('11124768',)
('79273990',)
('',)
('18666134',)
('',)
('21041702',)
('87473657',)
('77256179',)
('',)
('14878999',)
('',)
('47017418',)
('453113040',)
('',)
('13850997',)
('350908569',)
('45086286',)
('20377016',)
('20677285',)
('161273471',)
('60501251',)
('',)
('12575199',)
('34901386',)
('87958073',)
('9538810',)
('63636580',)
('',)
('11300939',)
('12296689',)
('15061828',)
('15115866',)
('368122058',)
('108247916',)
('57137983',)
('',)
('156538218',)
('46155357',)
('194551991',)
('10420158',)
('984441347',)
('',)
('',)
('',)
('',)
('',)
('',)
('26229154',)
('121887992',)
('127230701',)
('209616592',)
('11421979',)
('',)
('',)
('',)
('398964020',)
('514892632',)
('663427799',)
('856388544',)
('157293696',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('',)
('71745792',)
('157599454',)
('17878421',)
('299038367',)
('153551696',)
('44800017',)
('270476662',)
('53817837',)
('16096090',)
('29798918',)
('346141196',)
('40236006',)
('',)
('59444756',)
('185241782',)
('9772780',)
('15935881',)
('',)
('95918965',)
('635173912',)
('',)
('82057175',)
('',)
('16646246',)
('17605955',)
('12428202',)
('',)
('',)
('',)
('110058539',)
('',)
('',)
('',)
('184817065',)
('64002797',)
('139750768',)
('142218382',)
('',)
('7104008',)
('59239967',)
('21363568',)
('28090223',)
('34519906',)
('',)
('11240148',)
('13995939',)
('',)
('16676555',)
('50438096',)
('144986603',)
('199361625',)
('32250001',)
('15900672',)
('',)
('195734197',)
('',)
('12547788',)
('8727021',)
('7347310',)
('',)
('',)
('1160414452',)
('716691943',)
('979196144',)
('13091178',)
('',)
('1402824',)
('',)
('7604411',)
('',)
('',)
('',)
('',)
('42534198',)
('153033333',)
('',)
('40696491',)
('',)
('',)
('',)
('',)
('30381752',)
('',)
('',)
('28415690',)
('',)
('664553736',)
('414068424',)
('139611772',)
('304878598',)
('',)
('',)
('',)
('',)
('',)
('124467666',)
('40511348',)
('153303595',)
('10542911',)
('179579848',)
('275152110',)
('276221536',)
('17576685',)
('',)
('',)
('46208388',)
('975060248',)
('11205584',)
('207730504',)
('54150164',)
('',)
('205225152',)
('',)
('',)
('32322089',)
('',)
('60965959',)
('',)
('',)
('31974375',)
('',)
('45967752',)
('8430933',)
('42689012',)
('41874393',)
('54466992',)
('',)
('79051665',)
('10675735',)
('',)
('',)
('57994564',)
('55775421',)
('',)
('621349435',)
('56675008',)
('',)
('7384292',)
('140313303',)
('390865308',)
('74470119',)
('20000759',)
('140334038',)
('10153044',)
('9241961',)
('',)
('18536641',)
('12007686',)
('',)
('101643877',)
('60509333',)
('',)
('',)
('17965718',)
('898970103',)
('773591009',)
('24103027',)
('146791830',)
('100411567',)
('41869791',)
('',)
('106017161',)
('15648774',)
('',)
('395718493',)
('20907837',)
('128994958',)
('',)
('100090251',)
('18779751',)
('16300394',)
('',)
('',)
('304076819',)
('13194565',)
('110365357',)
('64119598',)
('148852384',)
('30588000',)
('99098862',)
('',)
('21610107',)
('',)
('',)
('57791989',)
('',)
('39498088',)
('165545183',)
('61375891',)
('',)
('282617163',)
('102306180',)
('',)
('20753238',)
('26146415',)
('9183139',)
('68441060',)
('227722489',)
('104517581',)
('131934735',)
('7893188',)
('',)
('261062592',)
('',)
('',)
('84081570',)
('89656801',)
('21324784',)
('77562605',)
('349720426',)
('36720946',)
('56945540',)
('58732451',)
('149733795',)
('128994100',)
('',)
('175238640',)
('13190190',)
('206954560',)
('184394356',)
('94968970',)
('576646665',)
('9425445',)
('27591108',)
('',)
('',)
('',)
('65388299',)
('57294616',)
('22992552',)
('17160635',)
('9384985',)
('68707182',)
('',)
('47589961',)
('333541869',)
('30849273',)
('212407228',)
('',)
('186363856',)
('',)
('83778021',)
('45043354',)
('208533950',)
('25874480',)
('20604131',)
('115427473',)
('77424457',)
('69095557',)
('',)
('141796238',)
('190520570',)
('',)
('49675618',)
('382107405',)
('',)
('126167964',)
('18402139',)
('',)
('83559
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
- [https://github.com/mariadb-corporation/maxscale-docker/blob/master/README.md](https://github.com/mariadb-corporation/maxscale-docker/blob/master/README.md)
