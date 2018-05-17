#!/usr/bin/env bash

IP=$1
MYPWD=`echo ~`

if [[ ! `grep "$1" "${MYPWD}/.ssh/config"` ]]; then
        sudo cat <<EOF >> ${MYPWD}/.ssh/config
Host $1
 HostName $1
 IdentityFile `echo ${MYPWD}`/.ssh/id_virtualskin_rsa
EOF
fi