import RPi.GPIO as GPIO
from time import sleep, time

# Tweezers should write out high all the time in loop
# Will complete circuits with the piece input pins
PIN_TWEEZERS = 2
# Success circuit power supply. Pin will output high in loop
PIN_SUCCESS_POS = 3
# Negative pin should be pulled down, and will trigger
# a message to Cloud indicating a successful piece removal
PIN_SUCCESS_NEG = 16
# All pieces should be pulled down and set to input
# They will create the circuits when touched by the tweezers
PIN_PIECE_0 = 0
PIN_PIECE_1 = 4
PIN_PIECE_2 = 5
PIN_PIECE_3 = 6
PIN_PIECE_4 = 7
PIN_PIECE_5 = 8
PIN_PIECE_6 = 9
PIN_PIECE_7 = 10
PIN_PIECE_8 = 11
PIN_PIECE_9 = 12
PIN_PIECE_10 = 14
PIN_PIECE_11 = 15
# The mosfet gate is controlled by this pin
PIN_BUZZER_CONTROL = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_TWEEZERS, GPIO.OUT)

GPIO.setup(PIN_SUCCESS_POS, GPIO.OUT)
GPIO.setup(PIN_SUCCESS_NEG, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(PIN_PIECE_0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_PIECE_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_PIECE_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_PIECE_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_PIECE_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_PIECE_5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_PIECE_6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_PIECE_7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_PIECE_8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_PIECE_9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_PIECE_10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_PIECE_11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(PIN_BUZZER_CONTROL, GPIO.OUT)

# Tweezers, and the success output pin both need
# to be high all the time to ensure
GPIO.output(PIN_TWEEZERS, GPIO.HIGH)
GPIO.output(PIN_SUCCESS_POS, GPIO.HIGH)

# The buzzer control we want low to start. Set it so to
# avoid drift. It may buzz momentarily on start, but
# that's acceptable.
GPIO.output(PIN_BUZZER_CONTROL, GPIO.LOW)


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

        if (GPIO.input()):
            print(f"Pin 0: {count}")
        elif (GPIO.input(4)):
            print(f"Pin 4: {count}")
        GPIO.output(1, GPIO.HIGH)

except KeyboardInterrupt:
    print("Qutting")
    GPIO.cleanup()
