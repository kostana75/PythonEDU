﻿a = int(input('Введите целое число: '))
if a < 0 and a % 2 == 0:
   print('отрицательное четное число')
elif a > 0 and a % 2 == 0: 
   print('положительное четное число')
elif a < 0 and a % 2 != 0:
   print('отрицательное нечетное число')
elif a > 0 and a % 2 != 0:
   print('положительное нечетное число') 
else:
   print('нулевое число')
