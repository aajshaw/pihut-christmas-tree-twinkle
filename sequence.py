from gpiozero import LEDBoard
import random
import time

# There are 25 LEDs on the tree, no LED on GPIO 3
LED_COUNT = 25
leds = (2,) + tuple(range(4, 28))

# Create an LEDBoard to represent the tree
tree = LEDBoard(*leds)

# Define the LEDs for each face of the tree
# starting with the face on the right
# when viewed from the HDMI port side of
# the Pi
face0 = (13, 10, 17)
face1 = (5, 3, 4)
face2 = (8, 2, 9)
face3 = (14, 1, 11)
face4 = (24, 15, 12)
face5 = (22, 21, 20)
face6 = (6, 19, 7)
face7 = (16, 23, 18)

faces = (face0, face1, face2, face3, face4, face5, face6, face7)

# Define the LEDs at the various levels
level0 = (0,) # top
level1 = (13, 5, 8, 14, 24, 22, 6, 16)
level2 = (10, 3, 2, 1, 15, 21, 19, 23)
level3 = (17, 4, 9, 11, 12, 20, 7, 18)

levels = (level0, level1, level2, level3)

def group_on(group):
    for led in group:
        tree.leds[led].on()

def group_off(group):
    for led in group:
        tree.leds[led].off()

def swirle(count):
    for ndx in range(0, count):
        group_off(faces[ndx % 8])
        group_off(faces[(ndx + 4) % 8])
        time.sleep(0.5)
        group_on(faces[ndx % 8])
        group_on(faces[(ndx + 4) %8])
    
    tree.on()

def layers(count):
    level = 0
    direction = 1
    for ndx in range(0, count):
        group_off(levels[level])
        time.sleep(0.5)
        group_on(levels[level])
        level += direction
        if level < 0:
            level = 1
            direction = 1
        if level > 3:
            level = 2
            direction = -1

def randomise(count):
    for ndx in range(0, count):
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

tree.on()

while True:
    swirle(random.randint(100, 200))
    layers(random.randint(100, 200))
    randomise(random.randint(300, 600))