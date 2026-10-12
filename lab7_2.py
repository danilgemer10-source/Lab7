import random
import string

print()

N = int(input('Введіть кількість номерів: '))

print()

leaters = string.ascii_uppercase

for i in range(N):
    number = random.randint(10000, 99999)

    результат = ''.join(random.choice(leaters) for _ in range(3))

    car_number = результат + str(number)

    print(f'{i + 1}. Автомобільний номер: {car_number}')




