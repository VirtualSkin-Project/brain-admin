#!/bin/bash

echo `which virtualenv`

if [[ ! `which nginx` ]]; then
    sudo apt install nginx
fi

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

curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt install -y nodejs
sudo npm install -g @angular/cli

#git clone https://github.com/VirtualSkin-Project/brain-front.git
#cd brain-front
#npm install package.json
#ng serve --host 0.0.0.0 --port 8000&
