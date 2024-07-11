import random

god_words = open("happy.txt", "r").read().splitlines()

for n in range(0, 30): print(random.choice(god_words).replace("_", " "), end=" ")
print("\n")
