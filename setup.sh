#!/bin/bash

sudo apt install nginx
sudo pip install virtualenv

virtualenv venv
`. venv/bin/activate`
venv/bin/pip install -r requirements.txt

venv/bin/python script.py

if [[ -f /etc/init.d/brain-manager ]]; then
	sudo rm /etc/init.d/brain-manager
fi
sudo cp brain-manager /etc/init.d/brain-manager
sudo update-rc.d brain-manager defaults
sudo systemctl start brain-manager.service

curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt install -y nodejs
sudo npm install -g @angular/cli

if [[ ! -d ./front ]]; then
	git clone https://github.com/VirtualSkin-Project/brain-front.git front
fi
cd front
npm install

PROCESS_PID="`ps -ef | grep 'ng serve --host 0.0.0.0 --port 80 --disable-host-check' | head -1 | awk '{print $2}'`"
if [[ ! $PROCESS_PID -eq "" ]]; then
	sudo kill $PROCESS_PID
fi
sudo ng serve --host 0.0.0.0 --port 80 --disable-host-check &
