pets = {}
while True:
    print("Введите данные о питомце (клавиша enter - выход):")
    name = input("Имя питомца: ")
    if not name:
        break
    pet_type = input("Вид питомца: ")
    age = int(input("Возраст питомца: "))
    owner = input("Имя владельца: ")
    year_case = ''
    if age % 10 == 1 and age != 11 and age % 100 != 11:
      year_case = 'год'
    elif 1 < age % 10 <= 4 and age != 12 and age != 13 and age != 14:
      year_case = 'года'
    else:
      year_case = 'лет'
    pets[name] = {
        'вид': pet_type,
        'возраст': f"{age} {year_case}",
        'владелец': owner
    }
p = list(pets.keys())
for value in pets.values():
    value
    print('Это ', value['вид'], ' по кличке "', *p,'". Возраст питомца: ', value['возраст'], '. Имя владельца: ', value['владелец'], sep = '')
