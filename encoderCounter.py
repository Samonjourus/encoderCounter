from RPi import GPIO
from time import sleep

clk1 = 16
dt1 = 19
clk2 = 20
dt2 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(clk2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter1 = 0
clkLastState1 = GPIO.input(clk)

counter2 = 0
clkLastState2 = GPIO.input(clk)

try:

        while True:
                clkState1 = GPIO.input(clk1)
                dtState1 = GPIO.input(dt1)
                clkState2 = GPIO.input(clk2)
                dtState2 = GPIO.input(dt2)
                if clkState1 != clkLastState1:
                        if dtState1 != clkState1:
                                counter1 += 1
                        else:
                                counter1 -= 1
                        print counter1
                clkLastState2 = clkState2
                if clkState2 != clkLastState2:
                        if dtState2 != clkState2:
                                counter2 += 1
                        else:
                                counter2 -= 1
                        print counter
                clkLastState1 = clkState1
                clkLastState2 = clkState2
                sleep(0.01)
finally:
