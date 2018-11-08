from RPi import GPIO
from time import sleep

clk = 26
dt = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

direction = ""

try:
    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
	    print "diff"
            if clkState:
		print "up"
                if dtState:
                    direction = "forward"
                    print direction
                else:
                    direction = "backwards"
                    print direction

        print str(clkState) + " " + str(dtState)

        clkLastState = clkState
        sleep(0.01)
	#print counter
finally:
        GPIO.cleanup()
