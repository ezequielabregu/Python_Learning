import random

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for index in range(5):
    rand1 = random.randint(0,2)
    rand2 = random.randint(0,2)
    print (f"[ {rand1}, {rand2} ] : {number_grid[rand1][rand2]}")
print("DONE")

