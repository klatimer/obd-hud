# Kenneth Latiemr
# 9/9/2017
# Description:
# 	main file for controlling the tachometer and character LCD.

import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import obd
import time
import threading

from led_tachometer import tachometer

global connection
global rpm

class led_thread(threading.Thread):
	def __init__(self):
		self.tach = tachometer()
		threading.Thread.__init__(self)
		self._running = True
	def run(self):
		global rpm
		while True:
			try:
				rpm = connection.query(obd.commands.RPM)
				self.tach.display_rpm(int(rpm.value.magnitude))
			except RuntimeError:
				self.tach.display_rpm(8000) # Turn on all leds
				pass

class lcd_thread(threading.Thread):
	def __init__(self):
		lcd_rs = 27
		lcd_en = 22
		lcd_d4 = 16
		lcd_d5 = 12
		lcd_d6 = 25
		lcd_d7 = 7
		lcd_backlight = 21
		lcd_columns = 16
		lcd_rows = 2
		self.lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
			   lcd_columns, lcd_rows, lcd_backlight)
		self.lcd.set_backlight(1)
		threading.Thread.__init__(self)
		self._running = True
	def run(self):
		global rpm
		global connection
		while True:
			try:
				if connection.status == OBDStatus.CAR_CONNECTED:
					self.lcd.message('%s %s' % ('RPM:\n', rpm))
				else:
					self.lcd.message('Connecting...')
				time.sleep(0.25)
			except RuntimeError:
				self.lcd.message('Error')
				pass

if __name__ == "__main__":
	connection = obd.OBD() # auto connect
	thread_2 = lcd_thread()
	thread_2.start()
	while connection.status == obd.OBDStatus.NOT_CONNECTED:
		time.sleep(0.1)
	thread_1 = led_thread()
	thread_1.start()
	
