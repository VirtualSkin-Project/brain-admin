#!/usr/bin/env bash

sshpass -f ./.limb ssh-copy-id -i $VIRTUALSKIN_USER_HOME/.ssh/id_virtualskin_rsa pi@$1
