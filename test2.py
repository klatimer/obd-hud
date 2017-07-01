# This script uses a loop to continuously print data from the car

import obd
import time

connection = obd.OBD()
cmd = obd.commands.RPM

while True:
	response = connection.query(cmd) # send command and parse response
	print(response.value)
	time.sleep(1)
