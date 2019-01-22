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

Running
=======
`make run` should start Flask API instance:
```
$ make run
pipenv run src/app.py
 * Serving Flask app "Reuters API" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:9666/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```

Endpoints
=========
* `/article/<newid>` - returns article by `newid` primary key
* `/articles[?filter1=value&filter1=value]` - returns a list of articles, optionally filtered by the filters:
  * exact match filters:
    * `cgisplit`
    * `lewissplit`
    * `newid`
    * `topics`
    * `oldid`
  * list filters (field should have all values):
    * `meta.companies`
    * `meta.exchanges`
    * `meta.orgs`
    * `meta.people`
    * `meta.places`
    * `meta.topics`
  * full-text filters (field should contain text):
    * `text.body`
    * `text.dateline`
    * `text.title`
  * date filters (article date should match one of):
    * `day` - same day of month
    * `month` - same month
    * `year` - same year
    * `date` - same date

Examples
========
Get article number 100 (i.e. `newid` is 100):
```
curl http://127.0.0.1:9666/article/100
```
Get all articles from 1987:
```
curl http://127.0.0.1:9666/article\?year\=1987
```
Get all articles about USA, Japan and Reagan from 1987:
```
curl http://127.0.0.1:9666/article\?year\=1987\&people\=reagan\&places\=usa,japan
```
Get all articles about USA, Japan and Reagan from 1987 which mention Exchange Commission:
```
curl http://127.0.0.1:9666/article\?year\=1987\&people\=reagan\&places\=usa,japan\&text.body\=Exchange%20Commission
```