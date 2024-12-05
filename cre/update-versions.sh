#!/bin/bash

VERSION_YEAR=${CRE_VERSION:0:4}
CURRENT_YEAR=$(date +'%Y')
COPY_FILES=false


if [ ! -z "$1" ]; then
  VERSION_YEAR=$1
  COPY_FILES=true
fi

if [ "$VERSION_YEAR" = "$CURRENT_YEAR" ]; then
  COPY_FILES=true
fi

echo "$(pwd)"

echo "$VERSION_YEAR $CURRENT_YEAR $COPY_FILES"

echo "cut -f2,3 /cre/versions.txt > cre/versions/versions_$VERSION_YEAR.txt"


if [ $COPY_FILES ]; then
  echo "cp /cre/requirements.txt.orig cre/versions/requirements_$VERSION_YEAR.txt"
fi

#       run: (cut -f2,3 /cre/versions.txt > cre/versions/versions_2024.txt)
#       run: (cp /cre/requirements.txt.orig cre/versions/requirements_2024.txt)


