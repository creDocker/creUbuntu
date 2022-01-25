#!/bin/bash

# Creates requirements.txt

if [ ! -f /cre/python/requirements.txt ]; then
    pip freeze > /cre/python/requirements.txt
fi

# https://github.com/bndr/pipreqs

pipreqs --mode gt --force /cre/python/
