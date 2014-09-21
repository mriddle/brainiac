[![Build Status](https://travis-ci.org/mriddle/brainiac.svg?branch=master)](https://travis-ci.org/mriddle/brainiac) [![Coverage Status](https://coveralls.io/repos/mriddle/brainiac/badge.png)](https://coveralls.io/r/mriddle/brainiac)

Brainiac
========

Assists with my learning of Python, basic data structures and algorithms. Will display a problem and verify your given answer

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone git@github.com:mriddle/brainiac.git
$ cd brainiac
$ pip install -r requirements.txt
$ find . -name '*.example' | grep '^[\.c]' | perl -pE 's/^(.*?)\.example/$1/' | xargs -IFILE cp -v FILE.example FILE
$ python manage.py syncdb
$ foreman start web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku run python manage.py syncdb
$ heroku open
```
