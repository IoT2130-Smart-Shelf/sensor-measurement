# Imports of the necessary libraries are carried out
import time
import busio
import adafruit_vl53l0x as av
from laser_linear import laser_linearization

# Initialize number pins of I2C
SCL = 3
SDA = 2

# Initialize I2C bus and sensor.
i2c = busio.I2C(SCL, SDA)
laser_sensor = av.VL53L0X(i2c)

while True:
    print("Range: {0}mm".format(laser_linearization(laser_sensor.range)))
    time.sleep(1.0)
