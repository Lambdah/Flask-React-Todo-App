#!/bin/bash

[[ "$VIRTUAL_ENV" == "" ]]; INVENV=$?
if [ $INVENV -eq 0 ]
then
    echo "changing environment"
    source ./venv/bin/activate
fi
export FLASK_APP=app.py
export FLASK_ENV=development
echo "Starting Server"
flask run