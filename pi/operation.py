import RPi.GPIO as GPIO

# Tweezers should write out high all the time in loop
# Will complete circuits with the piece input pins
PIN_TWEEZERS = 2
# Success circuit power supply. Pin will output high in loop
PIN_SUCCESS_POS = 3
# Negative pin should be pulled down, and will trigger
# a message to Cloud indicating a successful piece removal
PIN_SUCCESS_INPUT = 16
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
GPIO.setup(PIN_SUCCESS_INPUT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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

def activate_buzzer():
    GPIO.output(PIN_BUZZER_CONTROL, GPIO.HIGH)

def deactivate_buzzer():
    GPIO.output(PIN_BUZZER_CONTROL, GPIO.LOW)
