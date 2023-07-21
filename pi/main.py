from google.cloud import pubsub_v1
import RPi.GPIO as GPIO
# system libraries
import datetime
import logging
import sys
from time import sleep, time
# local libraries
import operation

# Set up logging. Debug messages will only go to stdout,
# but the rest will go to the file 'operation.log'
logger = logging.getLogger()
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
logger.addHandler(console_handler)
file_handler = logging.FileHandler('operation.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

# Set up pubsub globals
publisher = pubsub_v1.PublisherClient()
# TODO: Un-hardcode this topic
topic = publisher.topic_path('gweiss-simple-path', 'operation-test')

# Logging messages
MSG_NON_MATCHING_PINS = "The active pin doesn't match the triggered pin."

def send_pubsub_msg(pin):
    global publisher
    global topic
    countdown = 15
    data = f'{{ "local_time": "{datetime.datetime.now().isoformat()}", "pos": {str(pin)} }}'
    publisher.publish(topic, data.encode("utf-8"))

# In order to be sure all our pins have cleared setup, since
# a few of them start high or floating, we want to be sure
# we don't accidentally trigger any behaviors on startup
# so we'll sleep for a second on start of the script JUST in case
sleep(1.0)

active_pin = -1
active_time = -1
# reset timer is in milliseconds. We don't want to use sleep
# in any way in our loop because we want as much responsiveness
# as possible in the game system, so we rely on a time test
# in order to see when we want to re-enable a "failure" state
trigger_reset_time = 1500
try:
    while True:
        cur_time = round(time.time() * 1000)
        # if we have an active pin, short circuit things
        # so we don't go through the whole pin tests as
        # we have a pin triggered so we want to wait to
        # test anything to be sure we're not sending spam
        # messages to Pub/Sub for the same "failure"
        if active_pin != -1:
            if cur_time - trigger_reset_time < active_time:
                continue
            else:
                active_pin = -1
                active_time = -1
                continue

        if (GPIO.input(operation.PIN_ANKLE_TO_KNEE_BONE)):
            operation.activate_buzzer()
            # Sanity check, if this happens, we're probably
            # in a bad state. Reset, log and continue
            if active_pin != operation.PIN_ANKLE_TO_KNEE_BONE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_ANKLE_TO_KNEE_BONE}"
                logging.CRITICAL(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_ANKLE_TO_KNEE_BONE
            active_time = cur_time
            send_pubsub_msg(operation.PIN_ANKLE_TO_KNEE_BONE)
        elif (GPIO.input(operation.PIN_SPARE_RIBS)):
            operation.activate_buzzer()
            # Sanity check, if this happens, we're probably
            # in a bad state. Reset, log and continue
            if active_pin != operation.PIN_SPARE_RIBS:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_SPARE_RIBS}"
                logging.CRITICAL(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_SPARE_RIBS
            active_time = cur_time
            send_pubsub_msg(operation.PIN_SPARE_RIBS)
        elif (GPIO.input(operation.PIN_WRITERS_CRAMP)):
            operation.activate_buzzer()
            # Sanity check, if this happens, we're probably
            # in a bad state. Reset, log and continue
            if active_pin != operation.PIN_WRITERS_CRAMP:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_WRITERS_CRAMP}"
                logging.CRITICAL(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_WRITERS_CRAMP
            active_time = cur_time
            send_pubsub_msg(operation.PIN_WRITERS_CRAMP)
        elif (GPIO.input(operation.PIN_CHARLIE_HORSE)):
            operation.activate_buzzer()
            # Sanity check, if this happens, we're probably
            # in a bad state. Reset, log and continue
            if active_pin != operation.PIN_CHARLIE_HORSE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_CHARLIE_HORSE}"
                logging.CRITICAL(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_CHARLIE_HORSE
            active_time = cur_time
            send_pubsub_msg(operation.PIN_CHARLIE_HORSE)
        elif (GPIO.input(operation.PIN_BUTTERFLIES_IN_THE_STOMACH)):
            operation.activate_buzzer()
            # Sanity check, if this happens, we're probably
            # in a bad state. Reset, log and continue
            if active_pin != operation.PIN_BUTTERFLIES_IN_THE_STOMACH:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_BUTTERFLIES_IN_THE_STOMACH}"
                logging.CRITICAL(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_BUTTERFLIES_IN_THE_STOMACH
            active_time = cur_time
            send_pubsub_msg(operation.PIN_BUTTERFLIES_IN_THE_STOMACH)
        elif (GPIO.input(operation.PIN_BROKEN_HEART)):
            operation.activate_buzzer()
            # Sanity check, if this happens, we're probably
            # in a bad state. Reset, log and continue
            if active_pin != operation.PIN_BROKEN_HEART:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_BROKEN_HEART}"
                logging.CRITICAL(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_BROKEN_HEART
            active_time = cur_time
            send_pubsub_msg(operation.PIN_BROKEN_HEART)
        elif (GPIO.input(operation.PIN_WRENCHED_ANKLE)):
            operation.activate_buzzer()
            # Sanity check, if this happens, we're probably
            # in a bad state. Reset, log and continue
            if active_pin != operation.PIN_WRENCHED_ANKLE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_WRENCHED_ANKLE}"
                logging.CRITICAL(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_WRENCHED_ANKLE
            active_time = cur_time
            send_pubsub_msg(operation.PIN_WRENCHED_ANKLE)
        elif (GPIO.input(operation.PIN_ADAMS_APPLE)):
            operation.activate_buzzer()
            # Sanity check, if this happens, we're probably
            # in a bad state. Reset, log and continue
            if active_pin != operation.PIN_ADAMS_APPLE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_ADAMS_APPLE}"
                logging.CRITICAL(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_ADAMS_APPLE
            active_time = cur_time
            send_pubsub_msg(operation.PIN_ADAMS_APPLE)
        elif (GPIO.input(operation.PIN_FUNNY_BONE)):
            operation.activate_buzzer()
            # Sanity check, if this happens, we're probably
            # in a bad state. Reset, log and continue
            if active_pin != operation.PIN_FUNNY_BONE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_FUNNY_BONE}"
                logging.CRITICAL(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_FUNNY_BONE
            active_time = cur_time
            send_pubsub_msg(operation.PIN_FUNNY_BONE)
        elif (GPIO.input(operation.PIN_WATER_ON_THE_KNEE)):
            operation.activate_buzzer()
            # Sanity check, if this happens, we're probably
            # in a bad state. Reset, log and continue
            if active_pin != operation.PIN_WATER_ON_THE_KNEE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_WATER_ON_THE_KNEE}"
                logging.CRITICAL(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_WATER_ON_THE_KNEE
            active_time = cur_time
            send_pubsub_msg(operation.PIN_WATER_ON_THE_KNEE)
        elif (GPIO.input(operation.PIN_WISH_BONE)):
            operation.activate_buzzer()
            # Sanity check, if this happens, we're probably
            # in a bad state. Reset, log and continue
            if active_pin != operation.PIN_WISH_BONE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_WISH_BONE}"
                logging.CRITICAL(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_WISH_BONE
            active_time = cur_time
            send_pubsub_msg(operation.PIN_WISH_BONE)
        elif (GPIO.input(operation.PIN_BREAD_BASKET)):
            operation.activate_buzzer()
            # Sanity check, if this happens, we're probably
            # in a bad state. Reset, log and continue
            if active_pin != operation.PIN_BREAD_BASKET:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_BREAD_BASKET}"
                logging.CRITICAL(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_BREAD_BASKET
            active_time = cur_time
            send_pubsub_msg(operation.PIN_BREAD_BASKET)
        elif (GPIO.input(operation.PIN_SUCCESS_INPUT)):
            # Sanity check, if this happens, we're probably
            # in a bad state. Reset, log and continue
            if active_pin != operation.PIN_SUCCESS_INPUT:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_SUCCESS_INPUT}"
                logging.CRITICAL(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_SUCCESS_INPUT
            active_time = cur_time
            send_pubsub_msg(operation.PIN_SUCCESS_INPUT)

except KeyboardInterrupt:
    print("Qutting")
    GPIO.cleanup()
