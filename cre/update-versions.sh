#!/bin/bash
sleep 2

VERSION_YEAR=${CRE_VERSION:0:4}
CURRENT_YEAR=$(date +'%Y')
COPY_FILES=false

if [ ! -z "$1" ]; then
  VERSION_YEAR=$1
  COPY_FILES=true
fi

#Overwrite always during first year!
if [ "$VERSION_YEAR" = "$CURRENT_YEAR" ]; then
  COPY_FILES=true
fi

#Copy if not exists at all
if [ ! -f /cre/versions/requirements_$VERSION_YEAR.txt ]; then
  COPY_FILES=true
fi

#mkdir -p /cre/versions/

#Always use latest version
cut -f2,3 /cre/versions.txt > /cre/versions/versions_$VERSION_YEAR.txt

if [ $COPY_FILES ]; then
  echo cp /cre/requirements.txt.orig /cre/versions/requirements_$VERSION_YEAR.txt
fi



