# Sahur Timer / 1.1 / 11.09.2026

from time import sleep
import datetime
from os import system, mkdir
from sys import platform
import json 
from colorama import init, Fore, Back, Style

import time_calculator
import time_bigASCII

init()
#system('mode con: cols=60 lines=17')

remain_time = ['00:00:00', '000']

data = { 'dateTime' : "0000-00-00 00:00:00", 
         'mode' : 1 }

if platform == 'win32': clearOutput = "cls"
else: clearOutput = "clear"


def menu():
  try: 
    system(clearOutput)
    print(' [1] - Смотреть остаток \n [2] - Изменить дату \n [3] - Формат вывода \n [ ] - Выйти')
    de = input(" > ")
    return de        
  except KeyboardInterrupt: return 0

def output_mode():
  print(" [1] - Стандартный \n [2] - Бегущие строки \n [3] - Большой Аски")
  de = input(">> ")
  if de == '1': data['mode'] = 1
  if de == '2': data['mode'] = 2
  if de == '3': data['mode'] = 3
  print("ага, записано"); sleep(1)
  update_data = write()

def read():
  global data
  try: 
      with open('data/time.json', 'r') as file:
        new_data = json.load(file)
        data.clear(); data.update(new_data)
  except FileNotFoundError: 
      print("Ошибка: файл time.json не найден"); sleep(1); print('создан в локальной папке')
      create_data_file = write()

def write():
  with open('data/time.json', 'w') as file:
      json.dump(data, file, ensure_ascii=False, indent=4)
      print("данные сохранены!")
  print(data); sleep(1)

  
def write_time ():
  global data
  check_update_data = read()
  while True:
    #os.system('cls')
    new_dateTime = input("Новая дата (ГГГГ-ММ-ДД ЧЧ-ММ-СС): ")
    if new_dateTime == ' ': break

    if '-' in new_dateTime:
      if len(new_dateTime) == 19:
        if new_dateTime[5:7] != "00" and new_dateTime[8:10] != "00":
          if int(new_dateTime[5:7]) < 13 and int(new_dateTime[8:10]) < 32: 
            new_dateTime = new_dateTime.replace(".","-")
            data['dateTime'] = new_dateTime
            update_data = write()
            break
          else: print('ага, давай без несуществующих месяцев и дней'); sleep(1) 
        else: print('ага, давай без несуществующих месяцев и дней'); sleep(1) 
      else: print('неправильное количество символов!'); sleep(1)
    else: print('разделителей нету'); sleep(1)

    continue


def check():
    update_data = read()
    print(data)

    test = '01.08.2026 09:09:09'

    sleep(1)
    system(clearOutput)
    cycle = 0
    while True:
      cycle += 1
      try:
        #print(data['dateTime'])

        # 2. Превращаем текст в объект datetime
        # %d - день, %m - месяц, %Y - год (4 цифры), %H - часы, %M - минуты, %S - секунды
        target_time = datetime.datetime.strptime(data['dateTime'], "%Y-%m-%d %H-%M-%S")
        # 3. Получаем текущее время
        now = datetime.datetime.now()
        # 4. Проверяем, не в прошлом ли дата, и считаем разницу
        if target_time < now:
          if cycle < 2:
            print("Эта дата уже прошла!"); sleep(1.5)
            system(clearOutput)
          time_left = now - target_time
        else:
          time_left = target_time - now
        # 5. Извлекаем дни и считаем чистые часы, минуты и секунды
        days = time_left.days
        total_seconds = int(time_left.total_seconds())
        # Переводим остаток секунд в часы, минуты и секунды
        hours = (total_seconds // 3600) % 24
        minutes = (total_seconds // 60) % 60
        seconds = total_seconds % 60

        result = time_calculator.calculation(data['dateTime'], 1) # альтернативный вариант самоделка
        #print(result) отладка
        days = result[2]
        hours = result[3]
        minutes = result[4]
        seconds = result[5]

        # добавление нулей к одиночным цифрам
        #if len(str(days)) < 2: days = '0'+str(days)
        if hours < 10: hours = '0'+str(hours)
        if minutes < 10: minutes = '0'+str(minutes)
        if seconds < 10: seconds = '0'+str(seconds)
        # 6. Выводим красивый результат
        remain_time[0] = f"{hours}:{minutes}:{seconds}"
        remain_time[1] = days

        if int(remain_time[1]) > 10: color = Fore.GREEN
        if int(remain_time[1]) < 10: color = Fore.YELLOW 
        if int(remain_time[1]) < 3: color = Fore.RED 

        clock, days = remain_time
        l = '─' * len(str(remain_time[1]))
        if len(l) < 2: 
          l = '──'
          days = '0'+str(remain_time[1])

        def output_mode_1(color, days, clock):
          line1 = f"╭─{l}─╮╭──────────╮"
          line2 = f"│ {color}{days}{Style.RESET_ALL} ││ {color}{clock}{Style.RESET_ALL} │"
          line3 = f"╰─{l}─╯╰──────────╯"
          print(line1)
          print(line2)
          print(line3, end="", flush=True)
          print("\r\033[2F", end="", flush=True)


        def output_mode_2(color, days, clock):
          a1 = f"\r╭─{l}─╮╭──────────╮ \n│ {color}{days}{Style.RESET_ALL} ││ {color}{clock}{Style.RESET_ALL} │\n╰─{l}─╯╰──────────╯"
        
          if remain_time[0] == '00:00:00' and remain_time[1] == 0:
            print(a1, end="", flush=True); sleep(3)
            color = Fore.WHITE
            print(a1, end="", flush=True); sleep(1)
            print(Fore.WHITE,"\n  time is up",Style.RESET_ALL); sleep(5)
            input("< ")
            return 0

          print(a1, end="\r", flush=True)

        def output_mode_3(color, days, times):
          print(color, end="")
          time_bigASCII.main(result)
          

        if data['mode'] == 1: 
            output = output_mode_1(color, days, clock)
        if data['mode'] == 2: 
            output = output_mode_2(color, days, clock)
        if data['mode'] == 3: 
            output = output_mode_3(color, days, clock)
        sleep(1)
      except KeyboardInterrupt: 
        print(Fore.RESET)
        return True



if __name__ == '__main__':
  while True: # общий алгоритм
    check_data = read()
    a = menu()
    if a == '1':
      a = check()
      if a == True:
        continue
    elif a == '2':
      a = write_time()
    elif a == '3':
      a = output_mode()
    elif a == 'exit' or a == ' ':
      print("Выход"), sleep(0.5)
      break
    




