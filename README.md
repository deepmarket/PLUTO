[![Build Status](https://travis-ci.org/deepmarket/PLUTO.svg?branch=develop)](https://travis-ci.org/deepmarket/PLUTO)

## Overview

PLUTO is a cross platform desktop application that can be used to connect to the deepmarket network.

This project is in active development and is being maintained by the [team members](#team-members) listed below.
If you would like to submit changes, please open a pull request. Please read the [getting set up to develop locally](https://github.com/deepmarket/PLUTO/wiki/Setting-up-deepmarket's-api-backend-for-local-development) guide.


### Prerequisites 

#### Python

This project requires Python 3.6. Make sure python3.6 is installed before attempting any of this!

[Installer](https://www.python.org/downloads/release/python-366/)

To check version:

```bash
$ python3 --version
```

#### Docker

Docker is required for this project if you want to add resources to the Deepmarket Network.  To install docker, please follow the docker-mentation [located here](https://docs.docker.com/v17.09/engine/installation/).

## Installing, Testing, Running:

#### Installation

First you'll need to install the required dependencies.  We use the `pipenv` package management tool to make managing dependencies easier.  For more info on the tool, see [here](https://docs.pipenv.org/en/latest/basics/).  To install:
```bash
$ python3 -m pip install pipenv
```

Then to install dependencies:

```bash
$ pipenv install
```

If you receive an error related to the python binary, try:

```bash
$ pipenv install --python=$(which python3)

We use [fbs](https://github.com/mherrmann/fbs) as the application runtime.
It is recommended to run PLUTO by interacting with it's command line interface:

```bash
# Run the application
$ fbs run

```
You should now be running a development version of PLUTO!

## Developing

#### Runtime Environment

Use `pipenv` to activate a virtual environment necessary for running this project.  

```bash
$ pipenv shell
```

It is recommended that you read the [getting set up to develop locally](https://github.com/deepmarket/PLUTO/wiki/Setting-up-deepmarket's-api-backend-for-local-development) guide.


#### Testing

Testing is done using two libraries: Python's builtin `Unittest` for unit testing and `behave` for functional BDD tests.

They can be ran independently.  Make sure that the virtual environment has been activated before running these.

```bash
$ python -m unittest discover ./src/unittest/python
$ python -m behave ./src/integrationtest/python
```

Alternately, these can be run without running `pipenv shell` first:
```bash
$ pipenv run python -m unittest discover ./src/unittest/python
$ pipenv run python -m behave ./src/integrationtest/python
```

`pipenv run {cmd}`  will run the subsequent command within the virtual environment defined in the `Pipfile`.

#### Running the Application:

Note that you must be in the project root directory to run the project.  We use the [fman](https://build-system.fman.io/manual/) build tool for packaging, so from the root directory, simply: 

Either:
```bash
$ pienv shell
$ fbs run
```

or
```bash
$ pipenv run fbs run
```
Will spin up a local instance of the project!


#### TODOs
- Add mocks for integration tests
