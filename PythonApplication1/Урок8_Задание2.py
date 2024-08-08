n = int(input('Укажите количество чисел в массиве: ')) 
m = list(map(int, input().split()))
m.insert(0, m.pop()) 
print(*m)
