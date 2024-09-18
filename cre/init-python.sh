#!/bin/bash

# Creates requirements.txt

if [ ! -f /cre/python/requirements.txt ]; then
    #CURRENT_YEAR=$(date +'%Y')
    VERSION_YEAR=${CRE_VERSION:0:4}
    cp /cre/versions/requirements_$VERSION_YEAR.txt /cre/python/requirements.txt
    #pip3 freeze --no-cache-dir > /cre/python/requirements.txt
    chmod 777 /cre/python/requirements.txt
    # https://github.com/bndr/pipreqs
    ## pipreqs --mode gt --force /cre/python/
    ## pipreqs --mode compat --force /cre/python/
    pip3 install --no-cache-dir --root-user-action ignore -r /cre/python/requirements.txt
    echo "requirements.txt written"
fi

# Initialize
if [ -f /cre/python/initialize.sh ]; then
    chmod 777 /cre/python/initialize.sh
    /cre/python/initialize.sh
fi

# https://github.com/bndr/pipreqs
# Generate requirements.txt file for any project based on imports
## pipreqs --mode compat --force /cre/python/
cat /cre/python/requirements.txt
# For now: only compare:
pipreqs --mode compat --diff /cre/python/requirements.txt /cre/python/
pipreqs --mode compat --print /cre/python/

# Install
pip3 install --no-cache-dir --root-user-action ignore -r /cre/python/requirements.txt

# Run main.py or app.py or auto.py?



