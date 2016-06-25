#!/bin/bash

pid=$(ps -a|grep openvpn  | sed -e 's/^[[:space:]]*//' | cut -d" " -f1)
sudo kill -s 9 $pid
resolvconf -u
