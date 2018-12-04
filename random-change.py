from gpiozero import LEDBoard
import random
import time

# There are 25 LEDs on the tree, no LED on GPIO 3
LED_COUNT = 25
leds = (2,) + tuple(range(4, 28))

# Create an LEDBoard to represent the tree
tree = LEDBoard(*leds)

# All LEDs on
tree.on()

# Loop forever
while True:
    # Select 3 random LEDs
    led1 = random.randint(0, LED_COUNT - 1)
    led2 = random.randint(0, LED_COUNT - 1)
    led3 = random.randint(0, LED_COUNT - 1)

    # Turn the random LEDs off
    tree.leds[led1].off()
    tree.leds[led2].off()
    tree.leds[led3].off()

    # Sleep for a while
    time.sleep(0.25)

    # Turn the random LEDs back on
    tree.leds[led1].on()
    tree.leds[led2].on()
    tree.leds[led3].on()
    
