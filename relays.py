import RPi.GPIO as GPIO

#set GPIO mode to Broadcom SOC channel
GPIO.setmode(GPIO.BCM)
#GPIO pin that is labeled for Master Vavle (MV on relay)
mv = 2
gpio_pins = (3, 4, 5, 6, 7, 8, 9)
   
GPIO.setup(mv, GPIO.OUT)
GPIO.output(mv, GPIO.HIGH)

for pin in gpio_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

#turn on pins
def mv_on():
    GPIO.output(mv, GPIO.LOW)

def one_on():
    GPIO.output(gpio_pins[0], GPIO.LOW)

def two_on():
    GPIO.output(gpio_pins[1], GPIO.LOW)

def three_on():
    GPIO.output(gpio_pins[2], GPIO.LOW)

def four_on():
    GPIO.output(gpio_pins[3], GPIO.LOW)

def five_on():
    GPIO.output(gpio_pins[4], GPIO.LOW)

def six_on():
    GPIO.output(gpio_pins[5], GPIO.LOW)

def seven_on():
    GPIO.output(gpio_pins[6], GPIO.LOW)


#Turning off pins

def mv_off():
    GPIO.output(mv, GPIO.HIGH)

def one_off():
    GPIO.output(gpio_pins[0], GPIO.HIGH)

def two_off():
    GPIO.output(gpio_pins[1], GPIO.HIGH)

def three_off():
    GPIO.output(gpio_pins[2], GPIO.HIGH)

def four_off():
    GPIO.output(gpio_pins[3], GPIO.HIGH)

def five_off():
    GPIO.output(gpio_pins[4], GPIO.HIGH)

def six_off():
    GPIO.output(gpio_pins[5], GPIO.HIGH)

def seven_off():
    GPIO.output(gpio_pins[6], GPIO.HIGH)
