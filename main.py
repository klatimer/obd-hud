# Kenneth Latiemr
# 9/9/2017
# Description:
# 	main file for controlling the tachometer and character LCD.

import RPi.GPIO as GPIO
import Adafruit_Python_CharLCD as LCD
import obd
import time
import threading
import led_tachometer

global connection
global rpm

class led_thread(threading.Thread):
	def __init__(self):
		led_1 = 9
		led_2 = 11
		led_3 = 26
		led_4 = 19
		led_5 = 13
		led_6 = 6
		led_7 = 5
		led_8 = 0
		tach = tachometer([led_1, led_2, led_3, led_4, led_5, led_6, led_7, led_8])
		threading.Thread.__init__(self)
		self._running = True
	def run(self):
		global rpm
		try:
			while True:
				tach.display_rpm(rpm)
				time.sleep(0.1)
		except RuntimeError:
			tach.display_rpm(8000) # Turn on all leds
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
		lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
			   lcd_columns, lcd_rows, lcd_backlight)
		lcd.set_backlight(1)
		threading.Thread.__init__(self)
		self._running = True
	def run(self):
		global rpm
		try:
			while True:
				lcd.message('%s %s' % ('RPM:\n', rpm))
				time.sleep(0.25)
		except RuntimeError:
			lcd.message('Error')
			pass

if __name__ == "__main__":
	connection = obd.Async()
	def new_rpm(r):
		rpm = r.value # Write to global variable that both threads can access
	connection.watch(obd.commands.RPM, callback=new_rpm)
	connection.start()
	# Create threads
	led_thread = led_thread()
	lcd_thread = lcd_thread()
	# Start threads
	led_thread.start()
	lcd_thread.start()