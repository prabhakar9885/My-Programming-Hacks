
The script is meant for removing the human-effort that is involved in starting/stoping the VPN for getting connected to IIIT-Hyderabad network, from Ubuntu machine.

How to use?
==============
1. First setup the VPN by following the instructions from http://vpn.iiit.ac.in/
2. Create a file "/etc/openvpn/VPN.pass" and the user-name and password in the following format
    username
    password
3. At the end of the file "/etc/openvpn/linux_client.conf", add the following lines.
    #Password file
    auth-user-pass "./VPN.pass"
4. For starting the VPN: sudo bash start_vpn.sh
       stopping the VPN: sudo bash stop_vpn.sh
