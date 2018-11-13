from RPi import GPIO
from time import sleep

clk = 26
dt = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

forwardCcounter = 0
backwardCounter = 0
pulseCounter = 0;
clkLastState = GPIO.input(clk)

direction = ""

try:
    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState && (clkState != clkLastState):
            pulseCounter = pulseCounter + 1
            if dtState:
                if direction != "forward":
                    direction = "forward"
                    forwardCounter = forwardCounter+1
                    print direction + " " + str(forwardCounter)
                else:
                    counter = counter+1
                    print direction + " " + str(counter)
            else:
                if direction != "backward":
                    counter1 = counter1+1
                    direction = "backward"
                    print direction + " " + str(counter1)
                else:
                    counter1 = counter1+1
                    print direction + " " + str(counter)
        clkLastState = clkState
        sleep(0.001)
#print counter
finally:
GPIO.cleanup()
