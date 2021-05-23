# bounce.py
#
# Exercise 1.5
HEIGHT_LOOSING_RATIO = 3 / 5
JUMPS_TO_SHOW = 10

jump = 1
height = 100  # Meters

while jump <= JUMPS_TO_SHOW:
    height = height * HEIGHT_LOOSING_RATIO
    print(jump, round(height, 4))
    jump = jump + 1

