#!/bin/bash

set -e

pipenv run invoke clean
pipenv run invoke build
pipenv run invoke serve
