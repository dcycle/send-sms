#!/bin/bash
#
# Continuous integration script run on CircleCI, see ./.circleci/config.yml.
#
set -e

docker run --rm -v "$(pwd)":/app/code dcycle/python-lint:2 ./code
