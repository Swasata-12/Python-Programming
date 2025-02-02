# This file used as module to the exercise13 file

def find_max(numbers):
    maximum=numbers[0]
    minimum=numbers[0]
    for i in numbers:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    return maximum