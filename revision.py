from RPi import GPIO
from time import sleep

clk = 20
dt = 26

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
            if clkState:
                if dtState:
                    direction = "forward"
                    print direction
                else:
                    direction = "backwards"
                    print direction

	#print str(clkState2) + " " + str(dtState2)

        clkLastState = clkState
        sleep(0.01)
	#print counter
finally:
        GPIO.cleanup()