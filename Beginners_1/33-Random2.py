import random

class  Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second            # python los interpreta como una lista


dice = Dice()

for i in range(300):
    print(dice.roll())