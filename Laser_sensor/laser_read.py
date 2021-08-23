# Imports of the necessary libraries are carried out
import busio
import adafruit_vl53l0x as av
from laser_linear import laser_linearization
import requests

# api-endpoint
URL = "https://api.thingspeak.com/update.json?api_key=R6KP5RUYDZOS6XKO&/json"

# Initialize number pins of I2C
SCL = 3
SDA = 2

# Initialize I2C bus and sensor.
i2c = busio.I2C(SCL, SDA)
laser_sensor = av.VL53L0X(i2c)

# Read sensor
data_laser = laser_linearization(laser_sensor.range)

print("Range: {0}cm".format(data_laser))

PARAMS = { 
            "field2": laser_linearization(laser_sensor.range)}

# sending post request and saving the response as response object
r = requests.post(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()
print(data)