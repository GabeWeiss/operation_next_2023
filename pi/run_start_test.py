import RPi.GPIO as GPIO
import operation
import sys
from time import sleep, time

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
            sys.exit(1)

    sleep(1.0)

    piece_pin = operation.PIN_ANKLE_TO_KNEE_BONE
    piece_name = operation.pin_to_name(piece_pin)
    print(f"Confirm {piece_name} works by touching Tweezers to metal around piece.\nYou have 10 seconds to touch the metal before failure.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(piece_pin):
            break
        if round(time.time() * 1000) > start_time + 10000:
            print(f"Did not receive signal from {piece_name} within 10 seconds of test start.")
            sys.exit(1)

    sleep(1.0)

    piece_pin = operation.PIN_SPARE_RIBS
    piece_name = operation.pin_to_name(piece_pin)
    print(f"Confirm {piece_name} works by touching Tweezers to metal around piece.\nYou have 10 seconds to touch the metal before failure.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(piece_pin):
            break
        if round(time.time() * 1000) > start_time + 10000:
            print(f"Did not receive signal from {piece_name} within 10 seconds of test start.")
            sys.exit(1)

    sleep(1.0)

    piece_pin = operation.PIN_WRITERS_CRAMP
    piece_name = operation.pin_to_name(piece_pin)
    print(f"Confirm {piece_name} works by touching Tweezers to metal around piece.\nYou have 10 seconds to touch the metal before failure.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(piece_pin):
            break
        if round(time.time() * 1000) > start_time + 10000:
            print(f"Did not receive signal from {piece_name} within 10 seconds of test start.")
            sys.exit(1)

    sleep(1.0)

    piece_pin = operation.PIN_CHARLIE_HORSE
    piece_name = operation.pin_to_name(piece_pin)
    print(f"Confirm {piece_name} works by touching Tweezers to metal around piece.\nYou have 10 seconds to touch the metal before failure.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(piece_pin):
            break
        if round(time.time() * 1000) > start_time + 10000:
            print(f"Did not receive signal from {piece_name} within 10 seconds of test start.")
            sys.exit(1)

    sleep(1.0)

    piece_pin = operation.PIN_BUTTERFLIES_IN_THE_STOMACH
    piece_name = operation.pin_to_name(piece_pin)
    print(f"Confirm {piece_name} works by touching Tweezers to metal around piece.\nYou have 10 seconds to touch the metal before failure.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(piece_pin):
            break
        if round(time.time() * 1000) > start_time + 10000:
            print(f"Did not receive signal from {piece_name} within 10 seconds of test start.")
            sys.exit(1)

    sleep(1.0)

    piece_pin = operation.PIN_BROKEN_HEART
    piece_name = operation.pin_to_name(piece_pin)
    print(f"Confirm {piece_name} works by touching Tweezers to metal around piece.\nYou have 10 seconds to touch the metal before failure.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(piece_pin):
            break
        if round(time.time() * 1000) > start_time + 10000:
            print(f"Did not receive signal from {piece_name} within 10 seconds of test start.")
            sys.exit(1)

    sleep(1.0)

    piece_pin = operation.PIN_WRENCHED_ANKLE
    piece_name = operation.pin_to_name(piece_pin)
    print(f"Confirm {piece_name} works by touching Tweezers to metal around piece.\nYou have 10 seconds to touch the metal before failure.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(piece_pin):
            break
        if round(time.time() * 1000) > start_time + 10000:
            print(f"Did not receive signal from {piece_name} within 10 seconds of test start.")
            sys.exit(1)

    sleep(1.0)

    piece_pin = operation.PIN_ADAMS_APPLE
    piece_name = operation.pin_to_name(piece_pin)
    print(f"Confirm {piece_name} works by touching Tweezers to metal around piece.\nYou have 10 seconds to touch the metal before failure.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(piece_pin):
            break
        if round(time.time() * 1000) > start_time + 10000:
            print(f"Did not receive signal from {piece_name} within 10 seconds of test start.")
            sys.exit(1)

    sleep(1.0)

    piece_pin = operation.PIN_FUNNY_BONE
    piece_name = operation.pin_to_name(piece_pin)
    print(f"Confirm {piece_name} works by touching Tweezers to metal around piece.\nYou have 10 seconds to touch the metal before failure.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(piece_pin):
            break
        if round(time.time() * 1000) > start_time + 10000:
            print(f"Did not receive signal from {piece_name} within 10 seconds of test start.")
            sys.exit(1)

    sleep(1.0)

    piece_pin = operation.PIN_WATER_ON_THE_KNEE
    piece_name = operation.pin_to_name(piece_pin)
    print(f"Confirm {piece_name} works by touching Tweezers to metal around piece.\nYou have 10 seconds to touch the metal before failure.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(piece_pin):
            break
        if round(time.time() * 1000) > start_time + 10000:
            print(f"Did not receive signal from {piece_name} within 10 seconds of test start.")
            sys.exit(1)

    sleep(1.0)

    piece_pin = operation.PIN_WISH_BONE
    piece_name = operation.pin_to_name(piece_pin)
    print(f"Confirm {piece_name} works by touching Tweezers to metal around piece.\nYou have 10 seconds to touch the metal before failure.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(piece_pin):
            break
        if round(time.time() * 1000) > start_time + 10000:
            print(f"Did not receive signal from {piece_name} within 10 seconds of test start.")
            sys.exit(1)

    sleep(1.0)

    piece_pin = operation.PIN_BREAD_BASKET
    piece_name = operation.pin_to_name(piece_pin)
    print(f"Confirm {piece_name} works by touching Tweezers to metal around piece.\nYou have 10 seconds to touch the metal before failure.")
    start_time = round(time.time() * 1000)
    while True:
        if GPIO.input(piece_pin):
            break
        if round(time.time() * 1000) > start_time + 10000:
            print(f"Did not receive signal from {piece_name} within 10 seconds of test start.")
            sys.exit(1)

    sleep(1.0)

    print("All tests successfully passed.")
    GPIO.cleanup()
    sys.exit()
except:
    GPIO.cleanup()
    sys.exit(1)
