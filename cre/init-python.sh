#!/bin/bash

if [ $(echo " $CRE_VERSION < 2024.0" | bc) -eq 1 ] ; then
    /cre/init-python-old.sh
else
    /cre/init-python-uv.sh
fi




