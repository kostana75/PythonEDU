def fac(n):
  if n == 0:
    return 1
  return fac(n-1) * n

sp = []
y = int(input('Введите натуральное целое число: '))
for i in range(y, 0, -1):
  sp.append(fac(i))
print(sp)
