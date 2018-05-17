#!/usr/bin/env bash

IP=$1
MYPWD=`echo ~`

if [[ ! `grep "github.com" "${MYPWD}/.ssh/config"` ]]; then
        sudo cp ../deploy ${MYPWD}/.ssh/deploy
        sudo cat <<EOF >> ${MYPWD}/.ssh/config
Host $1
 HostName $1
 IdentityFile `echo ${MYPWD}`/.ssh/id_virtualskin_rsa
EOF
fi