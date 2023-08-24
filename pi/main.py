from google.cloud import pubsub_v1
import RPi.GPIO as GPIO
# system libraries
import datetime
import logging
import os
import sys
import time
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
publisher = None
topic = None
if "OPERATION_NO_PUBSUB" not in os.environ:
    publisher = pubsub_v1.PublisherClient()
    try:
        project_name = os.environ['OPERATION_PROJECT']
        topic_name = os.environ['OPERATION_TOPIC']

        topic = publisher.topic_path(project_name, topic_name)
    except:
        print("Environment not set for OPERATION_PROJECT and OPERATION_TOPIC (pubsub topic)")
        GPIO.cleanup()
        sys.exit(1)

# Logging messages
MSG_NON_MATCHING_PINS = "The active pin doesn't match the triggered pin."

def send_pubsub_msg(pin):
    # If we don't want to be sending things to pubsub because we're just testing
    # the system, then you can set this environment variable and everything else
    # should work, but no messages will be sent.
    if "OPERATION_NO_PUBSUB" in os.environ:
        return
    global publisher
    global topic
    countdown = 15
    data = f'{{ "local_time": "{datetime.datetime.now().isoformat()}", "pos": {str(pin)} }}'
    publisher.publish(topic, data.encode("utf-8"))

# In order to be sure all our pins have cleared setup, since
# a few of them start high or floating, we want to be sure
# we don't accidentally trigger any behaviors on startup
# so we'll sleep for a second on start of the script JUST in case
time.sleep(1.0)

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
            # If we're not getting signal from our active pin, we should
            # stop the motor regardless of our state of wanting to send
            # the message downstream.
            if not GPIO.input(active_pin):
                operation.deactivate_buzzer()
            else:
                operation.activate_buzzer()

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
            # Have to test against -1 because the first time we hit
            # an active pin, it's -1, and that's an acceptable state.
            if active_pin != -1 and active_pin != operation.PIN_ANKLE_TO_KNEE_BONE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_ANKLE_TO_KNEE_BONE}"
                logger.critical(msg)
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
            # Have to test against -1 because the first time we hit
            # an active pin, it's -1, and that's an acceptable state.
            if active_pin != -1 and active_pin != operation.PIN_SPARE_RIBS:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_SPARE_RIBS}"
                logger.critical(msg)
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
            # Have to test against -1 because the first time we hit
            # an active pin, it's -1, and that's an acceptable state.
            if active_pin != -1 and active_pin != operation.PIN_WRITERS_CRAMP:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_WRITERS_CRAMP}"
                logger.critical(msg)
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
            # Have to test against -1 because the first time we hit
            # an active pin, it's -1, and that's an acceptable state.
            if active_pin != -1 and active_pin != operation.PIN_CHARLIE_HORSE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_CHARLIE_HORSE}"
                logger.critical(msg)
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
            # Have to test against -1 because the first time we hit
            # an active pin, it's -1, and that's an acceptable state.
            if active_pin != -1 and active_pin != operation.PIN_BUTTERFLIES_IN_THE_STOMACH:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_BUTTERFLIES_IN_THE_STOMACH}"
                logger.critical(msg)
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
            # Have to test against -1 because the first time we hit
            # an active pin, it's -1, and that's an acceptable state.
            if active_pin != -1 and active_pin != operation.PIN_BROKEN_HEART:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_BROKEN_HEART}"
                logger.critical(msg)
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
            # Have to test against -1 because the first time we hit
            # an active pin, it's -1, and that's an acceptable state.
            if active_pin != -1 and active_pin != operation.PIN_WRENCHED_ANKLE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_WRENCHED_ANKLE}"
                logger.critical(msg)
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
            # Have to test against -1 because the first time we hit
            # an active pin, it's -1, and that's an acceptable state.
            if active_pin != -1 and active_pin != operation.PIN_ADAMS_APPLE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_ADAMS_APPLE}"
                logger.critical(msg)
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
            # Have to test against -1 because the first time we hit
            # an active pin, it's -1, and that's an acceptable state.
            if active_pin != -1 and active_pin != operation.PIN_FUNNY_BONE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_FUNNY_BONE}"
                logger.critical(msg)
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
            # Have to test against -1 because the first time we hit
            # an active pin, it's -1, and that's an acceptable state.
            if active_pin != -1 and active_pin != operation.PIN_WATER_ON_THE_KNEE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_WATER_ON_THE_KNEE}"
                logger.critical(msg)
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
            # Have to test against -1 because the first time we hit
            # an active pin, it's -1, and that's an acceptable state.
            if active_pin != -1 and active_pin != operation.PIN_WISH_BONE:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_WISH_BONE}"
                logger.critical(msg)
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
            # Have to test against -1 because the first time we hit
            # an active pin, it's -1, and that's an acceptable state.
            if active_pin != -1 and active_pin != operation.PIN_BREAD_BASKET:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_BREAD_BASKET}"
                logger.critical(msg)
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
            # Have to test against -1 because the first time we hit
            # an active pin, it's -1, and that's an acceptable state.
            if active_pin != -1 and active_pin != operation.PIN_SUCCESS_INPUT:
                msg = f"{MSG_NON_MATCHING_PINS}: Active: {active_pin}, Triggered: {operation.PIN_SUCCESS_INPUT}"
                logger.critical(msg)
                active_pin = -1
                active_time = -1
                continue

            # If we're here, it means this is the first time seeing
            # this pin trigger, so set the active pin and active time
            # so we don't repeat trigger a message
            active_pin = operation.PIN_SUCCESS_INPUT
            active_time = cur_time
            send_pubsub_msg(operation.PIN_SUCCESS_INPUT)
        else:
            operation.deactivate_buzzer()

except KeyboardInterrupt:
    print("Qutting")
    GPIO.cleanup()
except Exception as e:
    print(f"Exception: {e}")
    GPIO.cleanup()
