#!/usr/bin/env bash

sshpass -f ./.limb ssh-copy-id -i ~/.ssh/id_virtualskin_rsa pi@$1
