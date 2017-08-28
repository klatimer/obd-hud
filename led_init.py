# Kenneth Latimer
# 8/21/17
# Description
# 	Sets up LED pins and does a gauge sweep

import RPi.GPIO as GPIO
import time

def toggle_leds (led_pins, state): # state is GPIO.HIGH or GPIO.LOW
	for pin in led_pins:
		GPIO.output(pin, state)

def sweep_leds (led_pins, delay): # Turns on led_pins in sequence, leaving them on
	for pin in led_pins:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(delay)

delay = 0.2
GPIO.setmode(GPIO.BCM)
led_pins = [9, 11, 26, 19, 13, 6, 5, 0]
for pin in led_pins:
	GPIO.setup(pin, GPIO.OUT)
sweep_leds(led_pins, delay)
toggle_leds(led_pins, GPIO.LOW)
time.sleep(delay)
toggle_leds(led_pins, GPIO.HIGH)
time.sleep(2 * delay)
toggle_leds(led_pins, GPIO.LOW)

GPIO.cleanup() # remove eventually
