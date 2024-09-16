#!/bin/bash

# Creates requirements.txt



echo "Repository name: $GITHUB_REPOSITORY"

if [ ! -f /cre/python/requirements.txt ]; then
    pip3 freeze > /cre/python/requirements.txt
    chmod 777 /cre/python/requirements.txt
    # https://github.com/bndr/pipreqs
    pipreqs --mode gt --force /cre/python/
    echo "requirements.txt written"
fi

cat /cre/python/requirements.txt

# Install
pip3 install -r /cre/python/requirements.txt

# Initialize
if [ -f /cre/python/initialize.sh ]; then
    chmod 777 /cre/python/initialize.sh
    /cre/python/initialize.sh
fi

# Run main.py or app.py or auto.py?



