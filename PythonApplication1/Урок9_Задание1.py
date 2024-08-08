n = int(input('Введите количество элементов списка: '))
spisok = list(map(int, input('Введите числа через пробел - ').split()))[:n]
t = set(spisok)
print(len(t))
