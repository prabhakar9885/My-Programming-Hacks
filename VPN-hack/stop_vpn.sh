#!/bin/bash

pid=$(ps -a|grep openvpn | cut -d" " -f1)
sudo kill -s 9 $pid
resolvconf -u
