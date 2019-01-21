A homework for H2O.ai, based on [REQUIREMENTS.md](REQUIREMENTS.md)

Prerequisites
=============
A UNIX-like system with:
* Python 2.7
* [pipenv](https://pipenv.readthedocs.io/en/latest/)
* GNU make

Installation
============
1. clone repository
2. in the cloned directory, run
```
make install
```
It should create a virtualenv with Python 2.7, install all the dependencies and a pre-commit hook.

Testing
=======
`make lint` should execute the `pycodestyle` (former PEP8) checks on the code.

`make test` should execute the `py.test` and genarate spec-like output (using [pytest-spec](https://pypi.org/project/pytest-spec/))