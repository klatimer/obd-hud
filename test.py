# This is a test script to verify functionality of the packages installed

import obd

connection = obd.OBD() # auto-connects 
cmd = obd.commands.RPM # select an OBD command
response = connection.query(cmd)
print(response.value)
print(response.value.to("mph"))

