import RPi.GPIO as GPIO
import operation
import sys
from time import sleep, time

def exit_clean(err):
    GPIO.cleanup()
    sys.exit(err)

def test_piece(piece):
    piece_name = operation.pin_to_name(piece)
    print(f"Confirm {piece_name} works by touching Tweezers to metal around piece.\nYou have 10 seconds to touch the metal before failure.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(piece):
            break
        if round(time.time() * 1000) > start_time + 10000:
            print(f"Did not receive signal from {piece_name} within 10 seconds of test start.")
            exit_clean(1)

try:
    print("**** Starting Operation hardware validation test ****")

    sleep(1.0)

    print("Testing buzzer and red nose LED. Should buzz for 0.5 seconds.")

    sleep(1.0)

    operation.activate_buzzer()
    sleep(0.5)
    operation.deactivate_buzzer()
    sleep(1.0)

    print("Confirm success button works, and green light turns on.\nYou have 10 seconds to push the button.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(operation.PIN_SUCCESS_INPUT):
            print("Success button test passed.")
            break
        if round(time.time() * 1000) > start_time + 10000:
            print("Did not receive signal from the success button within 10 seconds of test start.")
            exit_clean(1)

    sleep(1.0)
    test_piece(operation.PIN_ADAMS_APPLE)
    sleep(1.0)
    test_piece(operation.PIN_WISH_BONE)
    sleep(1.0)
    test_piece(operation.PIN_BROKEN_HEART)
    sleep(1.0)
    test_piece(operation.PIN_FUNNY_BONE)
    sleep(1.0)
    test_piece(operation.PIN_SPARE_RIBS)
    sleep(1.0)
    test_piece(operation.PIN_BUTTERFLIES_IN_THE_STOMACH)
    sleep(1.0)
    test_piece(operation.PIN_WRITERS_CRAMP)
    sleep(1.0)
    test_piece(operation.PIN_BREAD_BASKET)
    sleep(1.0)
    test_piece(operation.PIN_CHARLIE_HORSE)
    sleep(1.0)
    test_piece(operation.PIN_ANKLE_TO_KNEE_BONE)
    sleep(1.0)
    test_piece(operation.PIN_WATER_ON_THE_KNEE)
    sleep(1.0)
    test_piece(operation.PIN_WRENCHED_ANKLE)
    sleep(1.0)

    print("All tests successfully passed.")
    exit_clean(0)
except:
    exit_clean(1)
