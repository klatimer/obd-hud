cd /
cd ~/python/obd_hud
sudo python led_init.py
sudo rfcomm bind rfcomm0 00:1D:A5:00:06:17
sudo python main.py
cd /
