#!/bin/bash

echo `which virtualenv`

if [[ ! `which virtualenv` ]]; then
    sudo pip install virtualenv
fi

virtualenv venv
`. venv/bin/activate`
venv/bin/pip install -r requirements.txt

venv/bin/python script.py

if [ -f /etc/init.d/brain-manager ] ; then
    sudo rm /etc/init.d/brain-manager
fi
sudo cp brain-manager /etc/init.d/brain-manager
sudo update-rc.d brain-manager defaults
sudo systemctl start brain-manager.service

sudo apt install -y npm
