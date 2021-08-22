import RPi.GPIO as GPIO
import time
import MySQLdb

db=MySQLdb.connect("localhost","root","carolina","sensing")

try:
    GPIO.setmode(GPIO.BCM)
    
    TRIG = 23
    ECHO = 24
    
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    GPIO.output(TRIG, GPIO.LOW)
    
    print("Waiting for sensor to settle")
    
    time.sleep(2)
    print("Calculating distance")
    
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)
    
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = round(pulse_duration*17150,2)
    print("Distance: ", distance," cm")
    
    insertrec=db.cursor()
    sqlquery="INSERT INTO distance(measure) VALUES ('"+str(distance)+"')"
    insertrec.execute(sqlquery)
    db.commit()
    print("Record saved succesfully")
    db.close()

finally:
    GPIO.cleanup()
