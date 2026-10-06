# Sahur Timer / 1.1 / 11.09.2026


import time
import datetime
import os
import json
from colorama import init, Fore, Back, Style

init()
os.system('mode con: cols=60 lines=17')

rem_time = ['00:00:00', '00']

data = { 'date' : "00.00.0000", 
         'time' : "00:00:00",
         'mode' : 1 }

def menu ():
  try: 
    os.system('cls')
    print(' [1] - Смотреть остаток \n [2] - Изменить дату \n [3] - Формат вывода \n [ ] - Выйти')
    de = input(" > ")
    return de        
  except KeyboardInterrupt: exit()

def output_mode ():
  print(" [1] - Стандартный \n [2] - Бегущие строки \n [3] - Большой Аски")
  de = input(">> ")
  if de == '1': data['mode'] = 1
  if de == '2': data['mode'] = 2
  if de == '3': data['mode'] = 3
  print("ага, записано"); time.sleep(1)
  update_data = write()

def read():
  global data
  try: 
      with open('time.json', 'r') as file:
        new_data = json.load(file)
        data.clear(); data.update(new_data)
  except FileNotFoundError: 
      print("Ошибка: файл time.json не найден"); time.sleep(1); print('создан в локальной папке')
      create_data_file = write()

def write():
  with open('time.json', 'w') as file:
      json.dump(data, file, ensure_ascii=False, indent=4)
      print("данные сохранены!")
  print(data); time.sleep(1)
  
  
def write_time ():
  global data
  check_update_data = read()
  while True:
    #os.system('cls')
    new_date = input("Новая дата (ДД-ММ-ГГГГ): ")
    if '-' not in new_date:
      print('разделителей нету'); time.sleep(1)
      continue
    if len(new_date) == 10:
      new_time = input("Новое время (ЧЧ-ММ-СС): ")
      if '-' not in new_date:
        print('разделителей нету'); time.sleep(1)
        continue
      if len(new_time) == 8:
        new_date = new_date.replace("-",".")
        new_time = new_time.replace("-",":")
        data['date'] = new_date
        data['time'] = new_time
        update_data = write()
        break
      else: 
        print('неправильное количество символов!'); time.sleep(1)
        continue
    else: print('неправильное количество символов!'); time.sleep(1)
    continue

def check ():
    update_data = read()
    print(data)
    time_x = data['date'].split('.')
    time_n = data['time'].split(':')
    print('date:', time_x)
    print('time:', time_n)

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


    test = '01.08.2026 09:09:09'
    time_data = data['date']+' '+data['time']
    print(time_data)
    time.sleep(1)
    os.system('cls')
    c = 0
    while True:
      c += 1
      try:
        # 2. Превращаем текст в объект datetime
        # %d - день, %m - месяц, %Y - год (4 цифры), %H - часы, %M - минуты, %S - секунды
        target_time = datetime.datetime.strptime(time_data, "%d.%m.%Y %H:%M:%S")
        # 3. Получаем текущее время
        now = datetime.datetime.now()
        # 4. Проверяем, не в прошлом ли дата, и считаем разницу
        if target_time < now:
          if c < 2:
            print("Эта дата уже прошла!")
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
        # добавление нулей к одиночным цифрам
        #if len(str(days)) < 2: days = '0'+str(days)
        if len(str(hours)) < 2: hours = '0'+str(hours)
        if len(str(minutes)) < 2: minutes = '0'+str(minutes)
        if len(str(seconds)) < 2: seconds = '0'+str(seconds)
        # 6. Выводим красивый результат
        rem_time[0] = f"{hours}:{minutes}:{seconds}"
        rem_time[1] = days

        if int(rem_time[1]) > 10: color = Fore.GREEN
        if int(rem_time[1]) < 10: color = Fore.YELLOW 
        if int(rem_time[1]) < 3: color = Fore.RED 

        times, days = rem_time
        l = '─' * len(str(rem_time[1]))
        if len(l) < 2: 
          l = '──'
          days = '0'+str(rem_time[1])

        def output_mode_1(color, days, times):
          line1 = f"╭─{l}─╮╭──────────╮"
          line2 = f"│ {color}{days}{Style.RESET_ALL} ││ {color}{times}{Style.RESET_ALL} │"
          line3 = f"╰─{l}─╯╰──────────╯"
          print(line1)
          print(line2)
          print(line3, end="", flush=True)
          print("\r\033[2F", end="", flush=True)


        def output_mode_2(color, days, times):
          a1 = f"\r╭─{l}─╮╭──────────╮ \n│ {color}{days}{Style.RESET_ALL} ││ {color}{times}{Style.RESET_ALL} │\n╰─{l}─╯╰──────────╯"
        
          if rem_time[0] == '00:00:00' and rem_time[1] == 0:
            print(a1, end="", flush=True); time.sleep(3)
            color = Fore.WHITE
            print(a1, end="", flush=True); time.sleep(1)
            print(Fore.WHITE,"\n  time is up",Style.RESET_ALL); time.sleep(5)
            input("< ")
            return 0

          print(a1, end="\r", flush=True)

        def output_mode_3(color, days, times):
          digits_2 = [
          [ "  ___",
            " /  /",
            "/__/ " ],
          [ "  _ ",
            "  / ",
            "_/_ " ],
          [ "  __",
            " __/",
            "/__ " ],
          [ "  __",
            " __/",
            "__/ " ],
          [ " _  ",
            "/__/",
            "  / " ],
          [ " __ ",
            "/__ ",
            "__/ " ],
          [ "  __",
            " /_ ",
            "/__/" ],
          [ " ___",
            "  _/",
            "  / " ],
          [ "  ___",
            " /__/",
            "/__/ " ],
          [ " ___",
            "/__/",
            "__/ " ],
      
          [ "   ",
            " - ",
            "-  " ]
        ]

          split_time_now = ['0','1',  '3','4',  '2','7']

          final_output = [0,0,0,0,0,0,0,0]

          digits = digits_2

          def calculation():
            time_now = str(datetime.datetime.now())[11:-7]
            b = time_now.split(':')
            #split_time_now[5] = list(b[2])[0]
            #split_time_now[5] = list(b[2])[1]
            split_time_now[0] = list(b[0])[0]
            split_time_now[1] = list(b[0])[1]
            split_time_now[2] = list(b[1])[0]
            split_time_now[3] = list(b[1])[1]
            split_time_now[4] = list(b[2])[0]
            split_time_now[5] = list(b[2])[1]
  
          get_calculation = calculation()
          for calc_digit in range(6):
            final_output[calc_digit] = digits[int(split_time_now[calc_digit])]
            
          LINE_1 = f"{color}{final_output[0][0]}{final_output[1][0]}{digits[10][0]}{final_output[2][0]}{final_output[3][0]}{digits[10][0]}{final_output[4][0]}{final_output[5][0]}\033[K"
          LINE_2 = f"{final_output[0][1]}{final_output[1][1]}{digits[10][1]}{final_output[2][1]}{final_output[3][1]}{digits[10][1]}{final_output[4][1]}{final_output[5][1]}\033[K"
          LINE_3 = f"{final_output[0][2]}{final_output[1][2]}{digits[10][2]}{final_output[2][2]}{final_output[3][2]}{digits[10][2]}{final_output[4][2]}{final_output[5][2]}\033[K"
          print(LINE_1)
          print(LINE_2)
          print(LINE_3, end="", flush=True)
          print("\r\033[3F", end="", flush=True)

        if data['mode'] == 1: 
            output = output_mode_1(color, days, times)
        if data['mode'] == 2: 
            output = output_mode_2(color, days, times)
        if data['mode'] == 3: 
            output = output_mode_3(color, days, times)
        time.sleep(1)
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
      print("Выход"), time.sleep(0.5)
      break
    




