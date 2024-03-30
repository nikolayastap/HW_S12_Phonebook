from HW_S12_Phonebook.Phonebook.input_data import input_data
from HW_S12_Phonebook.Phonebook.print_data import print_data
from HW_S12_Phonebook.Phonebook.change_data import change_data
from HW_S12_Phonebook.Phonebook.delete_data import delete_data

def interface():
  print("Добрый день! Вы попали в бот телефонный-справочник! \n"
        "1 - запись данных \n"
        "2 - вывод данных \n"
        "3 - изменение данных \n"
        "4 - удаление данных")
  command = int(input("Введите число: "))

  while command < 1 or command > 4:
    print("Неправильный ввод")
    command = int(input("Введите число: "))

  if command == 1:
    input_data()
  elif command == 2:
    print_data()
  elif command == 3:
    change_data()
  elif command == 4:
    delete_data()