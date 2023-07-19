import RPi.GPIO as GPIO
import operation
import sys
from time import sleep, time

print("**** Starting Operation hardware validation test ****")

sleep(1.0)

print("Testing buzzer and red nose LED. Should buzz for 0.5 seconds.")

sleep(1.0)

operation.activate_buzzer()
sleep(0.5)
operation.deactivate_buzzer()
sleep(1.0)

print("Confirm success button works, and green light turns on.")
start_time = round(time.time() * 1000)
while True:
    if GPIO.input(operation.PIN_SUCCESS_INPUT):
        break
    if round(time.time() * 1000) > start_time + 10000:
        print("Did not receive signal from the success button within 10 seconds of test start.")
        sys.exit(1)

sleep(1.0)

