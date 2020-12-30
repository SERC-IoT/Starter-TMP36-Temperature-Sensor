# micropython script for esp 8266 that reads the voltage from an analogue
# temperature sensor and convert that reading into degrees centigrade.
# 
# The TMP36 uses an analogue voltage with 10mV per degree resolution, with a
# 500mV offset to allow for negative temeratures.

import machine
import time

# setup analog input
sensor = machine.ADC(0)

# WeMos D1 mini has a voltage divider on the A0 input. This givens an input
# voltage range of around 3.0 to 3.2. Measurements have 10-bit depth.
voltage_range = 3.1 
value_range = 2**10

try:
    print("* TMP36 Temperature Readings *")
    while True:
        value = sensor.read()
        voltage = value * voltage_range / value_range
        temperature = (voltage - 0.5) * 100

        print("Voltage: {0:>5.3f} V. Temperature: {1:>5.3f} C".format(voltage, temperature), end='\r')

        time.sleep(1)

except KeyboardInterrupt:
    print('script stopped by user')
finally:
    print('Goodbye!')
