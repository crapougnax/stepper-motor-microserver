#!/bin/bash
export FLASK_APP=server.py
export FLASK_ENV=development

COMMAND=`which flask`

$COMMAND run --host=0.0.0.0