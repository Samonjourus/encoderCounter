from RPi import GPIO
from time import sleep

clk2 = 20
dt2 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter2 = 0
clkLastState2 = GPIO.input(clk2)

direction = ""

try:
    while True:
        clkState2 = GPIO.input(clk2)
        dtState2 = GPIO.input(dt2)
        if dtState2:
            direction="forward"
            print "forward"
        if clkState2:
            direction="backward"
            print "backward"
	#print str(clkState2) + " " + str(dtState2)
        if clkState2 != clkLastState2:
            if dtState2 != clkState2:
                counter2 += 1
            else:
                counter2 -= 1
        clkLastState2 = clkState2
        sleep(0.1)
	#print counter2
finally:
        GPIO.cleanup()
