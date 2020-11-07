import random

shells = {
    "L": random.randint(0, 1),
    "C": random.randint(0, 1),
    "R": random.randint(0, 1)
}

guess = input("Выберите напёрсток (L, C, R): ")

if shells[guess] == 1:
    print("Вы угадали!")
else:
    print("Увы, напёрсток пустой...")
