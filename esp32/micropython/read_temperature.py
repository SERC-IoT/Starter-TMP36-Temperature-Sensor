# micropython script for esp32 that reads the voltage from an analogue temperature
# sensor and convert that reading into degrees centigrade.
# 
# The TMP36 uses an analogue voltage with 10mV per degree resolution, with a
# 500mV offset to allow for negative temeratures.

import machine
import time

# define sensor pin
SENSOR_PIN = 35

# configure analog input settings
sensor = machine.ADC(machine.Pin(SENSOR_PIN))
sensor.atten(machine.ADC.ATTN_0DB)  # 1.2V range
sensor.width(machine.ADC.WIDTH_12BIT)   # value range 0 to 4095

voltage_range = 1.1
value_range = 2**12

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
