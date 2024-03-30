def print_data():
  print('Вывожу данные из 1 файла: \n')
  with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
    data_first = f.readlines()
    data_first_list = []
    j = 0
    for i in range(len(data_first)):
      if data_first[i] == '\n' or i == len(data_first) -1:
        data_first_list.append(''.join(data_first[j:i+1]))
        j = i
    print(''.join(data_first_list))

  print()
  print('Вывожу данные из 2 файла: \n')
  with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
    data_second = f.readlines()
    print(*data_second, end=' ')