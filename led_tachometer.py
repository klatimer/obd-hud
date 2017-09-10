# Kenneth Latimer
# 8/29/17
# Description:
# 	Class describing the RPM readout to the driver

import RPi.GPIO as GPIO
import math

class tachometer():
	def __init__(self, led_pins):
		self.led_pins = led_pins
		self.num_leds = len(led_pins)
		self.current_rpm = 0
		self.max_rpm = int(1000 * self.num_leds) # Using 1 LED per 1k RPM (for now)
		# Set up the GPIO
		GPIO.setmode(GPIO.BCM)
		for pin in led_pins:
			GPIO.setup(pin, GPIO.OUT)

	def display_rpm(self, current_rpm):
		self.clear_rpm()
		led_pins = self.led_pins
		num_leds_on = current_rpm / 1000 
		# Turn on the proper number of LEDs
		for i in range(num_leds_on):
			GPIO.output(led_pins[i], GPIO.HIGH)

	def clear_rpm(self):
		for pin in self.led_pins:
			GPIO.output(pin, GPIO.LOW)