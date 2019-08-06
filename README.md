[![Build Status](https://travis-ci.org/deepmarket/PLUTO.svg?branch=develop)](https://travis-ci.org/deepmarket/PLUTO)

## Overview

PLUTO is a cross platform desktop application that can be used to connect to the deepmarket network.

This project is in active development and is being maintained by the [team members](#team-members) listed below.
If you would like to submit changes, please open a pull request.

**Note**: This project requires Python 3.6+

#### Installing, Developing, and Testing:

First you'll need to install the required dependencies

```bash
$ python -m pip install -r requirements.txt
```

Next, you can read the [getting set up to develop locally](https://github.com/deepmarket/PLUTO/wiki/Setting-up-deepmarket's-api-backend-for-local-development) guide.

Testing is done using two libraries: Python's builtin `Unittest` for unit testing and `behave` for functional BDD tests.

They can be ran independently
```bash
$ python -m  unittest test/*.py

$ python -m behave test/features
```

#### Running the Application:

Note that you must be in the project root directory to run the project.

```bash
# Make sure you're using python 3.6+!
$ python src/main.py
```
