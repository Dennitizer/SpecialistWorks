import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)  #Red led
GPIO.setup(17,GPIO.OUT) #Green led
GPIO.setup(27,GPIO.OUT) #Blue led

A = True

while A == True:
    
    print "Green"
    GPIO.output(17,GPIO.HIGH)
    time.sleep(.100)
    print "-"
    GPIO.output(17,GPIO.LOW)
    time.sleep(.500)
    
    print "Red"
    GPIO.output(4,GPIO.HIGH)
    time.sleep(.100)
    print "-"
    GPIO.output(4,GPIO.LOW)
    time.sleep(.050)
    
    print "Red"
    GPIO.output(4,GPIO.HIGH)
    time.sleep(.100)
    print "-" 
    GPIO.output(4,GPIO.LOW)
    time.sleep(1.5)

    print "Green"
    GPIO.output(17,GPIO.HIGH)
    time.sleep(.100)
    print "-"
    GPIO.output(17,GPIO.LOW)
    time.sleep(.500)
    
    print "Blue"
    GPIO.output(27,GPIO.HIGH)
    time.sleep(.100)
    print "-"
    GPIO.output(27,GPIO.LOW)
    time.sleep(.050)
    
    print "Blue"
    GPIO.output(27,GPIO.HIGH)
    time.sleep(.100)
    print "-" 
    GPIO.output(27,GPIO.LOW)
    time.sleep(1.5)
   
    print "..."
    print " "
