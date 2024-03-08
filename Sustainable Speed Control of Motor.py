import RPi.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
in3 = 5
in4 = 6
en1 = 25
en2 = 26
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en1, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
p1 = GPIO.PWM(en1, 1000)
p2 = GPIO.PWM(en2, 1000)

p1.start(0)
p2.start(0)
print("\n")
print("The default speed & direction of the motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward e-exit")
print("\n")

battery_voltage = 5.0  # Assuming battery voltage in volts

while True:
    x = input()

    if x == 'r':
        print("run")
        if temp1 == 1:
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
            print("forward")
            x = 'z'
        else:
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            print("backward")
            x = 'z'

    elif x == 's':
        print("stop")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        x = 'z'

    elif x == 'e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

 # Calculate duty cycle based on battery voltage
    if battery_voltage > 9.6:
        duty_cycle = 100
    elif 9.6 >= battery_voltage >= 6:
        duty_cycle = 70
    else:
        duty_cycle = 50

    # Apply the calculated duty cycle to both motors
    p1.ChangeDutyCycle(duty_cycle)
    p2.ChangeDutyCycle(duty_cycle)

    print("Battery Voltage: {}V, Duty Cycle: {}%".format(battery_voltage, duty_cycle))

