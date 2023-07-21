import RPi.GPIO as GPIO

# TODO: need to map pieces to pins accurately. The following
# are not accurate yet.
PIN_ANKLE_TO_KNEE_BONE          = 9
PIN_SPARE_RIBS                  = 15
PIN_WRITERS_CRAMP               = 6
PIN_CHARLIE_HORSE               = 11
PIN_BUTTERFLIES_IN_THE_STOMACH  = 12
PIN_BROKEN_HEART                = 8
PIN_WRENCHED_ANKLE              = 5
PIN_ADAMS_APPLE                 = 7
PIN_FUNNY_BONE                  = 4
PIN_WATER_ON_THE_KNEE           = 0
PIN_WISH_BONE                   = 14
PIN_BREAD_BASKET                = 10

Piece_Names = {}
Piece_Names[PIN_ANKLE_TO_KNEE_BONE]         = "Ankle Bone is Connected to the Knee Bone"
Piece_Names[PIN_SPARE_RIBS]                 = "Spare Ribs"
Piece_Names[PIN_WRITERS_CRAMP]              = "Writer's Cramp"
Piece_Names[PIN_CHARLIE_HORSE]              = "Charlie Horse"
Piece_Names[PIN_BUTTERFLIES_IN_THE_STOMACH] = "Butterflies in the Stomach"
Piece_Names[PIN_BROKEN_HEART]               = "Broken Heart"
Piece_Names[PIN_WRENCHED_ANKLE]             = "Wrenched Ankle"
Piece_Names[PIN_ADAMS_APPLE]                = "Adam's Apple"
Piece_Names[PIN_FUNNY_BONE]                 = "Funny Bone"
Piece_Names[PIN_WATER_ON_THE_KNEE]          = "Water on the Knee"
Piece_Names[PIN_WISH_BONE]                  = "Wish Bone"
Piece_Names[PIN_BREAD_BASKET]               = "Bread Basket"

def pin_to_name(pin):
    try:
        return Piece_Names[pin]
    except:
        return None

# Tweezers should write out high all the time in loop
# Will complete circuits with the piece input pins
PIN_TWEEZERS = 2
# Success circuit power supply. Pin will output high in loop
PIN_SUCCESS_POS = 3
# Negative pin should be pulled down, and will trigger
# a message to Cloud indicating a successful piece removal
PIN_SUCCESS_INPUT = 16
# The mosfet gate is controlled by this pin
PIN_BUZZER_CONTROL = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_TWEEZERS, GPIO.OUT)

GPIO.setup(PIN_SUCCESS_POS, GPIO.OUT)
GPIO.setup(PIN_SUCCESS_INPUT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(PIN_ANKLE_TO_KNEE_BONE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_SPARE_RIBS, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_WRITERS_CRAMP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_CHARLIE_HORSE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_BUTTERFLIES_IN_THE_STOMACH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_BROKEN_HEART, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_WRENCHED_ANKLE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_ADAMS_APPLE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_FUNNY_BONE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_WATER_ON_THE_KNEE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_WISH_BONE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_BREAD_BASKET, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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
