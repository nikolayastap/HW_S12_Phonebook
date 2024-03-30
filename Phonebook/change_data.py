def change_data():
  var = int(input("Введите номер записи, которую Вы хотите изменить: "))
  var_format = int(input(f"В каком формате записать данные\n\n"
  f"1 Вариант: \n"
  f"name\nsurname\nphone\naddress\n\n"
  f"2 Вариант: \n"
  f"name;surname;phone;address\n\n"
  f"Выберете вариант: "))
  if var_format not in [1, 2]:
    print("Неправильный ввод")
    return

  if var_format == 1:
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
      data_first = f.readlines()
    data = [x.strip() for x in data_first]
    if var > len(data) // 4:
      print("Такой записи нет")
      return

    print("Введите новые данные:")
    name_new = input("Имя: ")
    surname_new = input("Фамилия: ")
    phone_new = input("Телефон: ")
    address_new = input("Адрес: ")

    idx = 6 * (var - 1)
    data[idx] = name_new
    data[idx + 1] = surname_new
    data[idx + 2] = phone_new
    data[idx + 3] = address_new

    with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
      f.write('\n'.join(data))
            
  elif var_format == 2:
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
      data_second = f.readlines()

    data = [x.strip().split(';') for x in data_second]

    if var > len(data):
      print("Такой записи нет")
      return

    print("Введите новые данные:")
    name_new = input("Имя: ")
    surname_new = input("Фамилия: ")
    phone_new = input("Телефон: ")
    address_new = input("Адрес: ")

    data[var - 1] = [name_new, surname_new, phone_new, address_new]

    with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
      for line in data:
        f.write(';'.join(line) + '\n')