# propa

[![Build Status](https://secure.travis-ci.org/michaeljoseph/propa.png)](http://travis-ci.org/michaeljoseph/propa)
[![Stories in Ready](https://badge.waffle.io/michaeljoseph/propa.png?label=ready)](https://waffle.io/michaeljoseph/propa) [![pypi version](https://badge.fury.io/py/propa.png)](http://badge.fury.io/py/propa)
[![# of downloads](https://pypip.in/d/propa/badge.png)](https://crate.io/packages/propa?version=latest)
[![code coverage](https://coveralls.io/repos/michaeljoseph/propa/badge.png?branch=master)](https://coveralls.io/r/michaeljoseph/propa?branch=master)

## Overview

Python Library Boilerplate contains all the boilerplate you need to create a Python package.

* features
* and stuff 

## Usage

Install `propa`:

    pip install propa

## Documentation

[API Documentation](http://propa.rtfd.org)

## Testing

Install development requirements:

    pip install -r requirements.txt

Tests can then be run with:

    nosetests

Lint the project with:

    flake8 propa tests

## API documentation

Generate the documentation with:

    cd docs && PYTHONPATH=.. make singlehtml

To monitor changes to Python files and execute flake8 and nosetests
automatically, execute the following from the root project directory:

    stir