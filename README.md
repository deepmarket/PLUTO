[![Build Status](https://travis-ci.org/deepmarket/PLUTO.svg?branch=develop)](https://travis-ci.org/deepmarket/PLUTO)

## Overview

PLUTO is a cross platform desktop application that can be used to connect to the deepmarket network.

This project is in active development and is being maintained by the [team members](#team-members) listed below.
If you would like to submit changes, please open a pull request. Please read the [getting set up to develop locally](https://github.com/deepmarket/PLUTO/wiki/Setting-up-deepmarket's-api-backend-for-local-development) guide.


**Note**: This project requires Python 3.6. Make sure python3.6 is installed before attempting any of this!

[Installer](https://www.python.org/downloads/release/python-366/)

To check version:

```bash
$ python3.6 --version
Python 3.6.6
```

## Installing, Testing, Running:

#### Installation

First you'll need to install the required dependencies.  We use the `pipenv` package management tool to make managing dependencies easier.  For more info on the tool, see [here](https://docs.pipenv.org/en/latest/basics/).  To install:
```bash
$ python3.6 -m pip install pipenv
```

Then to install dependencies:

```bash
$ pipenv install
```

#### Runtime Environment

Use `pipenv` to activate a virtual environment necessary for running this project.  

```bash
$ pipenv shell
```

#### Testing

Testing is done using two libraries: Python's builtin `Unittest` for unit testing and `behave` for functional BDD tests.

They can be ran independently.  Make sure that the virtual environment has been activated before running these.

```bash
$ python -m unittest discover ./src/unittest/python

$ python -m behave ./src/integrationtest/python
```

#### Running the Application:

Note that you must be in the project root directory to run the project.  We use the [fman](https://build-system.fman.io/manual/) build tool for packaging, so from the root directory, simply: 
```bash
$ fbs run
```
Will spin up a local instance of the project!
