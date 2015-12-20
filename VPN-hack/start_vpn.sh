#!/bin/bash

cd /etc/openvpn/
openvpn --config linux_client.conf &

sleep 4

cp /etc/resolv.conf /etc/resolv_bck.conf 

echo "nameserver 10.4.20.204" > /etc/IIIT_namespace.conf
cat /etc/IIIT_namespace.conf /etc/resolv_bck.conf >/etc/resolv.conf

sleep 2
echo "VPN started"
