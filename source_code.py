
import time
import datetime
import os
import json
from colorama import init, Fore, Back, Style
init()
os.system('mode con: cols=60 lines=17')

# │─╭╮╰╯
rem_time = ['00:00:00', '00']
a = f"\r╭─────────────╮ \n│ {Fore.GREEN}{rem_time[0]}{Style.RESET_ALL} │\n╰─────────────╯"
b = f"\r╭─────────────╮ \n│ {Fore.GREEN}{rem_time[0]}{Style.RESET_ALL} │\n╰─────────────╯"
c = f"\r╭─────────────╮ \n│ {Fore.RED}{rem_time[0]}{Style.RESET_ALL} │\n╰─────────────╯"

a1 = f"\r╭────╮╭──────────╮ \n│ {Fore.GREEN}{rem_time[1]}{Style.RESET_ALL} ││ {Fore.GREEN}{rem_time[0]}{Style.RESET_ALL} │\n╰────╯╰──────────╯"
a2 = f"\r╭────╮╭──────────╮ \n│ {Fore.YELLOW}{rem_time[1]}{Style.RESET_ALL} ││ {Fore.YELLOW}{rem_time[0]}{Style.RESET_ALL} │\n╰────╯╰──────────╯"
a3 = f"\r╭────╮╭──────────╮ \n│ {Fore.RED}{rem_time[1]}{Style.RESET_ALL} ││ {Fore.RED}{rem_time[0]}{Style.RESET_ALL} │\n╰────╯╰──────────╯"

def menu ():
    os.system('cls')
    print(' [1] - Смотреть остаток \n [2] - Изменить дату \n [3] - Выйти')
    de = input(" > ")
    return de        

def write ():
  try:
   with open('time.json', 'r') as file:
     time_z = file.read()
  except: print("Ошибка: файл time.json не найден"), time.sleep(1), print('создан в локальной папке')
  while True:
    #os.system('cls')
    new_date = input("Новая дата (01.01.2001): ")
    if '.' not in new_date:
      print('точек нету')
      continue
    if len(new_date) == 10:
      new_time = input("Новое время (00:00:00): ")
      if '.' not in new_date:
        print('двоиточий нету')
        continue
      if len(new_time) == 8:
        data = { 'date' : new_date, 
                 'time' : new_time  }
        with open('time.json', 'w') as file:
          json.dump(data, file, ensure_ascii=False, indent=4)
        print("данные сохранены!")
        print(data), time.sleep(1)
        break
      else: 
        print('неправильное количество символов!'), time.sleep(1)
        continue
    else: print('неправильное количество символов!'), time.sleep(1)
    continue

def check ():
  try:
    with open('time.json', 'r') as file:
      time_z = json.load(file)
  except: print("Ошибка: файл time.json не найден")
  else:
    print(time_z)
    time_x = time_z['date'].split('.')
    time_n = time_z['time'].split(':')
    print('date:',time_x)
    print('time:',time_n)

    end_time = {'year':None, 'month':None, 'day':None, 'hour':None, 'minutes':None, 'seconds':None}

    end_time['year'] = time_x[0]
    end_time['month'] = time_x[1]
    end_time['day'] = time_x[2]
    end_time['hour'] = time_n[0]
    end_time['minutes'] = time_n[1]
    end_time['seconds'] = time_n[2]

    print(end_time)


    for j in end_time.values():
        print('\r',j, end="", flush=True)
        if j == None:
          print('\nнайдено: None')
          break
    else: print("\nне найдено")


    from datetime import datetime
    test = '01.08.2026 09:09:09'
    time_data = time_z['date']+' '+time_z['time']
    print(time_data)
    time.sleep(1)
    c = 0
    while True:
     c += 1
     try:
      # 2. Превращаем текст в объект datetime
      # %d - день, %m - месяц, %Y - год (4 цифры), %H - часы, %M - минуты, %S - секунды
      target_time = datetime.strptime(time_data, "%d.%m.%Y %H:%M:%S")
      # 3. Получаем текущее время
      now = datetime.now()
      # 4. Проверяем, не в прошлом ли дата, и считаем разницу
      if target_time < now:
          if c < 2:
           print("Эта дата уже прошла!")
          time_left = now - target_time
          status = "прошло"
      else:
          time_left = target_time - now
          status = "осталось"
      # 5. Извлекаем дни и считаем чистые часы, минуты и секунды
      days = time_left.days
      total_seconds = int(time_left.total_seconds())
      # Переводим остаток секунд в часы, минуты и секунды
      hours = (total_seconds // 3600) % 24
      minutes = (total_seconds // 60) % 60
      seconds = total_seconds % 60
      # добавление нулей к одиночным цифрам
      #if len(str(days)) < 2: days = '0'+str(days)
      if len(str(hours)) < 2: hours = '0'+str(hours)
      if len(str(minutes)) < 2: minutes = '0'+str(minutes)
      if len(str(seconds)) < 2: seconds = '0'+str(seconds)
      # 6. Выводим красивый результат
      v = f"{hours}:{minutes}:{seconds}"
      b = days
      rem_time[0] = v
      rem_time[1] = b
      a1 = f"\r╭────╮╭──────────╮ \n│ {Fore.GREEN}{rem_time[1]}{Style.RESET_ALL} ││ {Fore.GREEN}{rem_time[0]}{Style.RESET_ALL} │\n╰────╯╰──────────╯"
      a2 = f"\r╭────╮╭──────────╮ \n│ {Fore.YELLOW}{rem_time[1]}{Style.RESET_ALL} ││ {Fore.YELLOW}{rem_time[0]}{Style.RESET_ALL} │\n╰────╯╰──────────╯"
      a3 = f"\r╭────╮╭──────────╮ \n│ {Fore.RED}{rem_time[1]}{Style.RESET_ALL} ││ {Fore.RED}{rem_time[0]}{Style.RESET_ALL} │\n╰────╯╰──────────╯"
      a4 = f"\r╭────╮╭──────────╮ \n│ {Fore.RED}  {Style.RESET_ALL} ││ {Fore.RED}        {Style.RESET_ALL} │\n╰────╯╰──────────╯"
     except ValueError:
      print("\nОшибка! Вы ввели дату в неверном формате. Попробуйте еще раз.")
     try:
      if len(str(rem_time[1])) < 2:
        a1 = f"\r╭────╮╭──────────╮ \n│ {Fore.GREEN}0{rem_time[1]}{Style.RESET_ALL} ││ {Fore.GREEN}{rem_time[0]}{Style.RESET_ALL} │\n╰────╯╰──────────╯"
        a2 = f"\r╭────╮╭──────────╮ \n│ {Fore.YELLOW}0{rem_time[1]}{Style.RESET_ALL} ││ {Fore.YELLOW}{rem_time[0]}{Style.RESET_ALL} │\n╰────╯╰──────────╯"
        a3 = f"\r╭────╮╭──────────╮ \n│ {Fore.RED}0{rem_time[1]}{Style.RESET_ALL} ││ {Fore.RED}{rem_time[0]}{Style.RESET_ALL} │\n╰────╯╰──────────╯"
      if len(str(rem_time[1])) > 2:
        a1 = f"\r╭─────╮╭──────────╮ \n│ {Fore.GREEN}{rem_time[1]}{Style.RESET_ALL} ││ {Fore.GREEN}{rem_time[0]}{Style.RESET_ALL} │\n╰─────╯╰──────────╯"
        a2 = f"\r╭─────╮╭──────────╮ \n│ {Fore.YELLOW}{rem_time[1]}{Style.RESET_ALL} ││ {Fore.YELLOW}{rem_time[0]}{Style.RESET_ALL} │\n╰─────╯╰──────────╯"
        a3 = f"\r╭─────╮╭──────────╮ \n│ {Fore.RED}{rem_time[1]}{Style.RESET_ALL} ││ {Fore.RED}{rem_time[0]}{Style.RESET_ALL} │\n╰─────╯╰──────────╯"
      if rem_time[0] == '00:00:00' and rem_time[1] == 0:
        print(a4, end="", flush=True), time.sleep(3)
        print(a1, end="", flush=True), time.sleep(1)
        print(Fore.WHITE,"\n  time is up",Style.RESET_ALL), time.sleep(5)
        input()
        break
      #if len(str(rem_time[1])) < 2 and int(rem_time[0][6:]) < 11:
      #  for c1 in range(10):
      #    a3 = a4 = f"\r╭────╮╭──────────╮ \n│ {Fore.RED}  {Style.RESET_ALL} ││ {Fore.RED}        {Style.RESET_ALL} │\n╰────╯╰──────────╯"
      #    print(a3, end="\r", flush=True), time.sleep(0.5)
      #    a3 = a3 = f"\r╭────╮╭──────────╮ \n│ {Fore.RED}0{rem_time[1]}{Style.RESET_ALL} ││ {Fore.RED}{rem_time[0]}{Style.RESET_ALL} │\n╰────╯╰──────────╯"
      #    print(a3, end="\r", flush=True), time.sleep(0.5)

      if int(rem_time[1]) > 10:
        print(a1, end="\r", flush=True)
      if int(rem_time[1]) < 10 and int(rem_time[1]) > 3:
        print(a2, end="\r", flush=True)
      if int(rem_time[1]) < 3:
        print(a3, end="\r", flush=True)
      time.sleep(1)
     except: return True

    #a_1()


while True: # общий алгоритм
  a = menu()
  if a == '1':
    a = check()
    if a == True:
      continue
  elif a == '2':
    a = write()
  elif a == '3':
    print("Выход"), time.sleep(0.5)
    break
    




