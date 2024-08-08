x = int(input('Введите число: ' ))
k = 0
for d in range(1, x + 1):
  if x % d == 0:
    k += 1
print(k)
