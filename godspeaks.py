import random

god_words = open("happy.txt", "r").read().splitlines()

print(end="God says... ")

for n in range(0, 30): print(random.choice(god_words), end=" ")
print("\n")
