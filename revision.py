from RPi import GPIO
from time import sleep

clk = 26
dt = 20

global ecount
global ecount2
ecount =0
ecount2 =0

def my_callback(i):
	global ecount
	ecount = ecount+1
	print 'x '+str(ecount)
def my_callback2(i):
	global ecount2
	ecount2 = ecount2+1
	print 'y '+str(ecount2)

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(26, GPIO.RISING, callback=my_callback)
GPIO.add_event_detect(20, GPIO.RISING, callback=my_callback2)

forwardCounter = 0
backwardCounter = 0
pulseCounter = 0;
clkLastState = GPIO.input(clk)

direction = ""

try:
    while True:
        clkState = GPIO.input(clk)
#	print str(clkState)
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
        sleep(0.01)
#print counter
finally:
	GPIO.cleanup()
