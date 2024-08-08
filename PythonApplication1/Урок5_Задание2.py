s = input('Введите слово из маленьких латинских букв: ')
print('Количество гласных букв в слове: ', s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u'))
print('Количество согласных букв в слове: ', len(s) - (s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')))
if s.count('a') == 0:
  print('Гласной буквы a в слове', s, 'False')
if s.count('e') == 0:
  print('Гласной буквы e в слове', s, 'False')
if s.count('i') == 0:
  print('Гласной буквы i в слове', s, 'False')
if s.count('o') == 0:
  print('Гласной буквы o в слове', s, 'False')
if s.count('u') == 0:
  print('Гласной буквы u в слове', s, 'False')
