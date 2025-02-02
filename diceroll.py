# Write a code for dise roll using random module

import random
# dise1=random.randint(1,6)
# dise2=random.randint(1,6)
# print(f"({dise1},{dise2})")


class Dice:
    def roll(self):
        x=random.randint(1,6)
        y=random.randint(1,6)
        print(f"({x},{y})")


dise1=Dice()
# dise2=Dice()
dise1.roll()
# dise2.roll()
