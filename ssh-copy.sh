#!/usr/bin/env bash

echo -e `cat ./.limb` | ssh-copy-id -i ~/.ssh/id_virtualskin_rsa pi@$1