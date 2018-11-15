from RPi import GPIO
from time import sleep

clk = 26
dt = 20

def my_callback(i):
	print "x"

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(26, GPIO.RISING, callback=my_callback, bouncetime=1)

forwardCounter = 0
backwardCounter = 0
pulseCounter = 0;
clkLastState = GPIO.input(clk)

direction = ""

try:
    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState and (clkState != clkLastState):
            pulseCounter = pulseCounter + 1
            print "total pulses:  " + str(pulseCounter)
            if dtState:
                if direction != "forward":
                    direction = "forward"
                    forwardCounter = forwardCounter+1
                    print direction + " pulses: " + str(forwardCounter)
                else:
                    forwardCounter = forwardCounter+1
                    print direction + " pulses: " + str(forwardCounter)
            else:
                if direction != "backward":
                    backwardCounter = backwardCounter+1
                    direction = "backward"
                    print direction + " pulses: " + str(backwardCounter)
                else:
                    backwardCounter = backwardCounter+1
                    print direction + " pulses: " + str(backwardCounter)
        clkLastState = clkState
        #sleep(0.001)
#print counter
finally:
	GPIO.cleanup()
