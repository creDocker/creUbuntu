#!/bin/bash

/cre/gen-template.sh /cre/mq/create-queue.sh.tmpl &
/cre/gen-template.sh /cre/mq/consume-queue.sh.tmpl &
/cre/gen-template.sh /cre/mq/publish-queue.sh.tmpl &
/cre/gen-template.sh /cre/mq/length-queue.sh.tmpl &

wait


