# This script uses a loop to continuously print data from the car

import obd
import time

connection = obd.OBD()
cmd = obd.commands.SPEED

while True:
	response = connection.query(cmd) # send command and parse response
	print(response.value.to("mph"))
	time.sleep(0.5)
