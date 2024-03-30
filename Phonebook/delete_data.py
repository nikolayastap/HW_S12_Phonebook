def delete_data():
  var = int(input(f"В каком файле удалить запись?\n\n"
        f"1 Вариант (Файл 'data_first_variant.csv'): \n"
        f"{'name'}\n{'surname'}\n{'phone'}\n{'address'}\n\n"
        f"2 Вариант (Файл 'data_second_variant.csv'): \n"
        f"{'name'};{'surname'};{'phone'};{'address'}\n"
        f"Выберите вариант: "))

  while var != 1 and var != 2:
    print("Неправильный ввод")
    var = int(input("Введите число: "))

  n = int(input("\n Какую запись вы хотите удалить? \n Введите номер записи: "))

  if var == 1:
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
      data_first = f.readlines()
      j = 0
      data_first_list = []
      for i in range(len(data_first)):
        if data_first[i] == '\n' or i == len(data_first) - 1:
          data_first_list.append(''.join(data_first[j:i + 1]))
          j = i
      data_first_list_final = []
      for i in range(len(data_first_list)):
        if data_first_list[i] != '\n\n':
          data_first_list_final.append(data_first_list[i])
      data_first_list2 = data_first_list_final[:n - 1] + data_first_list_final[n:]
    with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_first_list2)
  elif var == 2:
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
      data_second = f.readlines()
      data_second_list = data_second[:n - 1] + data_second[n:]
    with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
      f.writelines(data_second_list)