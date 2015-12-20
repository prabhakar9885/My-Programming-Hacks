# Resets the Unity desktop envornment logs off the user account.
#!/bin/bash
dconf reset -f /org/compiz/
setsid unity &
sleep 2
exit
