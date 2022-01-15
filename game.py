import os
import random

# Бумага побеждает камень («бумага обёртывает камень»).
# Камень побеждает ножницы («камень затупляет или ломает ножницы»).
# Ножницы побеждают бумагу («ножницы разрезают бумагу»).

# В каждом раунде дается балл одному из игроков, в случае ничьи - балла нет.

# По завершению 3х раундов выводится результат: Победа, Проигрыш или Ничья с конкретным счетом(например: “Победа компьютера! Счет: 3/0”)


def game(move1, move2):
  if move1 == move2:
    print("Ничья.")
    return 0
  elif (move1 == "камень" and move2 == "ножницы") or (move1 == "бумага" and move2 == "камень") or (move1 == "ножницы" and move2 == "бумага"):
    print("В этом раунде победил первый игрок.")
    return 1
  elif (move2 == "камень" and move1 == "ножницы") or (move2 == "бумага" and move1 == "камень") or (move2 == "ножницы" and move1 == "бумага"):
    print("В этом раунде победил второй игрок.")
    return 2
  else:
    print("Что-то пошло не так.")
    return -1


def move_res(res, move1, move2):
  if res == 1:
    if move1 == "камень":
      print("Камень ломает ножницы.")
    elif move1 == "ножницы":
      print("Ножницы разрезают бумагу.")
    else:
      print("Бумага обёртывает камень.")
  else:
    if move2 == "камень":
      print("Камень ломает ножницы.")
    elif move2 == "ножницы":
      print("Ножницы разрезают бумагу.")
    else:
      print("Бумага обёртывает камень.")


def choice():
  print('Вы можете выбрать камень, ножницы или бумагу. Для выбора введите (1) "камень", (2) "ножницы" или (3) "бумага".')
  move = str(input("Введите свой выбор: "))
  move = move.lower()  # text.lower()
  if move == "1":
    move = "камень"
  elif move == "2":
    move = "ножницы"
  elif move == "3":
    move = "бумага"
  while move != "камень" and move != "ножницы" and move != "бумага":
    print("Такого варианта нет, попробуйте ещё раз.")
    move = str(input())
  return move


def win(count1, count2):
  if count1 == 3 or (count1 == 2 and count2 == 0):
    return 1
  elif count2 == 3 or (count2 == 2 and count1 == 0):
    return 2


def сomputer_choice():
  choose = ["камень", "бумага", "ножницы"]
  random.shuffle(choose)
  move = random.choice(choose)
  return move


print('Добро пожаловать в игру "камень-ножницы-бумага"! \nЧто Вы хотите сделать?')
print('\t 1 - начать новую игру \n \t 2 - выйти.')
exit = int(input())
while (exit != 1) and (exit != 2):
  print('Такого варианта нет, попробуйте ещё раз.')
  print('\t 1 - начать новую игру \n \t 2 - выйти.')
  exit = int(input())

while exit == 1:
  print('Выберите режим: \n \t 1 - игра с другим игроком \n \t 2 - игра с компьютером \n \t 3 - выйти из игры \n Для выбора введите цифру режима.')
  mode = int(input())
  #игра с другим игроком
  if mode == 1:
    name1 = input("Введите имя первого игрока:")
    name2 = input("Введите имя второго игрока:")

    count1, count2, round = 0, 0, 1
    while count1 != 3 and count2 != 3 and not (count1 == 2 and count2 == 0) and not (count2 == 2 and count1 == 0):
      print("Начало {3} раунда! Счёт {1}:{2}, ходит {0}.".format(
          name1, count1, count2, round))

      move1 = str(choice())

      os.system('CLS')

      print("Ход {0}!".format(name2))
      move2 = str(choice())

      #происходит игра
      os.system('CLS')
      print(
          "Выбор {0} - {2}, выбор {1} - {3}".format(name1, name2, move1, move2))
      res = int(game(move1, move2))
      if res != 0:
        move_res(res, move1, move2)

      #итог раунда
      if res == 0:
        round += 1
        continue
      if res == -1:
        break
      elif res == 1:
        count1 += 1
        round += 1
      else:
        count2 += 1
        round += 1
      print("Счёт {0}:{1}".format(count1, count2))
    print("Игра завершена!")
    check = win(count1, count2)
    if check == 1:
      print("Победителем является {0}.".format(name1))
    else:
      print("Победителем является {0}.".format(name2))
    menu_exit = 0
    while menu_exit != 1:
      print("Для продолжения введите 1: ")
      menu_exit = int(input())
      if menu_exit != 1:
        print("Мы так не играем.")
    os.system('CLS')

  #игра с компьютером​
  elif mode == 2:
    name1 = input("Введите имя первого игрока: ")
    name2 = "computer"

    count1, count2, round = 0, 0, 1
    while count1 != 3 and count2 != 3 and not (count1 == 2 and count2 == 0) and not (count2 == 2 and count1 == 0):
      print("Начало {3} раунда! Счёт {1}:{2}, ходит {0}.".format(
          name1, count1, count2, round))

      move1 = str(choice())

      print("Ход {0}!".format(name2))
      move2 = str(сomputer_choice())

      #происходит игра
      print(
          "Выбор {0} - {2}, выбор {1} - {3}".format(name1, name2, move1, move2))
      res = int(game(move1, move2))
      if res != 0:
        move_res(res, move1, move2)

      #итог раунда
      if res == 0:
        round += 1
        continue
      if res == -1:
        break
      elif res == 1:
        count1 += 1
        round += 1
      else:
        count2 += 1
        round += 1
      print("Счёт {0}:{1}".format(count1, count2))
    print("Игра завершена!")
    check = win(count1, count2)
    if check == 1:
      print("Победителем является {0}.".format(name1))
    else:
      print("Победителем является {0}.".format(name2))
    menu_exit = 0
    while menu_exit != 1:
      print("Для продолжения введите 1: ")
      menu_exit = int(input())
      if menu_exit != 1:
        print("Мы так не играем.")
    os.system('CLS')

  elif mode == 3:
    exit = 2
    break

  #ошибка
  else:
    print("Такого варианта нет, попробуйте ещё раз.")
    print('Выберите режим: \n \t 1 - игра с другим игроком \n \t 2 - игра с компьютером \n Для выбора введите цифру режима.')
    mode = int(input)

#выход​ ​ ​
if exit == 2:
  print('Хорошего Вам дня.')
#   import sys
#   sys.exit(0)
#завершить работу
