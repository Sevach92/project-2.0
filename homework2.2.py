first = int(input('Введите целое число: '))
second = int(input('Введите целое число: '))
third = int(input('Введите целое число: '))
if first == second == third:
    print(3)
elif first == third or first == second or second == third:
    print(2)
elif first != second != third:
    print(0)