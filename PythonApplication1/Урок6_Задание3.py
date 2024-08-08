a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))
for i in range(a, b + 1):
  if i % 2 == 0:
    print(i, end = ' ')
