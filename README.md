[![Build Status](https://travis-ci.org/deepmarket/PLUTO.svg?branch=develop)](https://travis-ci.org/deepmarket/PLUTO)

## Overview

PLUTO is a cross platform desktop application that can be used to connect to the deepmarket network.

This project is in active development and is being maintained by the [team members](#team-members) listed below.
If you would like to submit changes, please open a pull request.

**Note**: This project requires Python 3.6+

### Installing, Developing, and Testing:

#### Installing 

The project depends on python 3.6. Python 3.7 should be supported but is not yet thoroughly tested.

We use [pipenv](https://github.com/pypa/pipenv) to manage our dependencies which can be found in the [Pipfile](Pipfile).

We also recommend you to install [pipx](https://github.com/pipxproject/pipx) and subsequently pipenv.

This can be done by doing the following:

```bash
# Install pipx to the local users account
$ python -m pip install --user pipx

# Install pipenv via pipx (ensures package isolation)
$ python -m pipx install pipenv

# Install dependencies in Pipfile
$ pipenv install

# Start a venv with dependencies loaded
$ pipenv shell
```

We use [fbs](https://github.com/mherrmann/fbs) as the application runtime.
It is recommended to run PLUTO by interacting with it's command line interface:

```bash
# Run the application
$ fbs run
```
You should now be running a development version of PLUTO!

#### Developing

Next, you can read the [getting set up to develop locally](https://github.com/deepmarket/PLUTO/wiki/Setting-up-deepmarket's-api-backend-for-local-development) guide.

#### Testing

Testing is done using two libraries: Python's builtin `Unittest` for unit testing and `behave` for functional BDD tests.

They can be ran independently
```bash
$ python -m  unittest test/*.py

$ python -m behave test/features
```


