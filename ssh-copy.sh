#!/usr/bin/env bash

sshpass -f ./.limb ssh-copy-id -i /home/pi/.ssh/id_virtualskin_rsa pi@$1
