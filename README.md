[![Build Status](https://travis-ci.org/shared-systems/api.svg?branch=master)](https://travis-ci.org/shared-systems/api)

#### Synopsis
**Share Resources** is an open source platform designed to allow 
dynamic contribution and consumption of distributed computing resources.
Using a barter based system it allows a user to offer their own computational 
resources in exchange for tokens or use the resources of others in _the pool_.

This project is in active development and is being maintained by the [team members](#team-members) listed below.
If you would like to submit changes, please open a pull request.

#### Required Backend Dependencies
* MongoDB _3.0.15_
* Nodejs _8.11.1_
_-- Node Modules --_
* ExpressJs _4.16.2_ 
* mongoose _5.1.1_
* jsonwebtoken _8.2.0_
* bcrypt _2.4.3_
* body-parser _1.18.2_
* **Oh yea, and _ES6_**

_To see a full list of current dependencies (including dev) run `npm list --depth=0`

##### To install:
```bash
$ npm install
```

##### To run:
```bash
# Start mongo daemon
$ mongod

# Start node server
$ npm app.js
```

#### Required Frontend Dependencies
* Python _3.6_
* PyQt _5.10_
* sip _4.19.7_
* requests _2.18.4_

#### To install:
```bash
$ pip install -r requirements.txt
```

#### Team Members:
* [Susham Yerabolu](mailto:yerabolu@pdx.edu)
* [Haritha Munagala](mailto:mharitha@pdx.edu)
* [Soyoung Kim](mailto:soyoung@pdx.edu)
* [Sam Gomena](mailto:gomenas@pdx.edu)
* [Martin Li](mailto:xuanzhe@pdx.edu)