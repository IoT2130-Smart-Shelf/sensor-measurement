# Imports of the necessary libraries are carried out
import requests

# api-endpoint
URL = "https://api.thingspeak.com/update.json?api_key=R6KP5RUYDZOS6XKO&/json"

data_laser = 0
data_ultrasound = 0
time = "2019-04-23 21:36:20"
PARAMS = { 
        "created_at": time, # si se quiere mandar el tiempo, si no se manda toma el actual 
        "field1": data_ultrasound, 
        "field2": data_laser}

# sending post request and saving the response as response object
r = requests.post(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()
print(data)