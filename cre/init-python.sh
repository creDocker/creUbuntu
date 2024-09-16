#!/bin/bash

# Creates requirements.txt

if [ ! -f /cre/python/requirements.txt ]; then
    pip freeze > /cre/python/requirements.txt
    chmod 777 /cre/python/requirements.txt
    # https://github.com/bndr/pipreqs
    pipreqs --mode gt --force /cre/python/
    echo "requirements.txt written"
fi

cat /cre/python/requirements.txt

# Install
pip install -r /cre/python/requirements.txt

# Initialize
if [ -f /cre/python/initialize.sh ]; then
    chmod 777 /cre/python/initialize.sh
    /cre/python/initialize.sh
fi

# Run main.py or app.py or auto.py?



