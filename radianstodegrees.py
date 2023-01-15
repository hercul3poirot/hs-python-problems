from math import pi

def radians_to_degrees(number):
    converted = number * (180/pi)
    return round(converted, 1)


