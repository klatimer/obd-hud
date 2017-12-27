#/bin/sh
# launcher.sh
# navigate to home, then to this directory, then run a python script
# make sure to edit /etc/rc.local as root and add the following:
# 	su - pi -c "bash /home/pi/path-to-this-file/launcher.sh &"

cd /
cd ~/python/obd_hud
sudo python led_init.py
sudo rfcomm bind rfcomm0 00:1D:A5:00:06:17
sudo python main.py
cd /
