summa = int(input('Минимальная сумма инвестиций: '))
mike = int(input('Количество долларов у Майкла: '))
ivan = int(input('Количество долларов у Ивана: '))
if (mike >= summa) and (ivan >= summa):
  print(2)
elif (mike >= summa) and (ivan <= summa):
  print('Mike')
elif (mike <= summa) and (ivan >= summa):
  print("Ivan")
elif (mike <= summa) and (ivan <= summa) and ((mike + ivan) >= summa):
  print(1)
elif (mike <= summa) and (ivan <= summa) and ((mike + ivan) <= summa):
  print(0)
