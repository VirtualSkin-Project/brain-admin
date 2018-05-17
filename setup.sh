#!/bin/bash

echo `which virtualenv`

if [[ ! `which virtualenv` ]]; then
    sudo pip install virtualenv
fi

virtualenv venv
`. venv/bin/activate`
venv/bin/pip install -r requirements.txt

venv/bin/python script.py

