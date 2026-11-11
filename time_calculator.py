# calculator of time by caktuz / 1.0 / 06.11.2026

import time
import datetime 


def calculation(time_end, format_number) :
  def check_days_in_month_and_year(year_number, month_number): # счёт дней в месяце и проверка на високосный год
    if month_number in (1, 3, 5, 7, 8, 10, 12): days_in_month = 31
    if month_number in (4, 6, 9, 11): days_in_month = 30

    if month_number == 2: # проверка на високосный год и счёт дней в феврале
      if (year_number % 4 == 0 and year_number % 100 != 0) or (year_number % 400 == 0): days_in_year = 366; days_in_month = 29
      else: days_in_year = 365; days_in_month = 28

    if (year_number % 4 == 0 and year_number % 100 != 0) or (year_number % 400 == 0): days_in_year = 366
    else: days_in_year = 365

    return days_in_year, days_in_month

  def days_in_prev_month(year, month):
    if month == 1:
        return check_days_in_month_and_year(year - 1, 12)
    return check_days_in_month_and_year(year, month - 1)

  time_now = str(datetime.datetime.now()) # я знаю что можно без этих костылей, но так не интересно 
  time_now_list = [time_now[0:4], time_now[5:7], time_now[8:10], time_now[11:13], time_now[14:16], time_now[17:19]] # разделение строки текущего времени на элементы
  time_end_list = [time_end[0:4], time_end[5:7], time_end[8:10], time_end[11:13], time_end[14:16], time_end[17:19]] # разделение строки конечного времени на элементы
  remain_list = [int(time_end_list[0])-int(time_now_list[0]), int(time_end_list[1])-int(time_now_list[1]), int(time_end_list[2])-int(time_now_list[2]), int(time_end_list[3])-int(time_now_list[3]), int(time_end_list[4])-int(time_now_list[4]), int(time_end_list[5])-int(time_now_list[5])] # оставшееся количество времени 
  
  #if time_now_list >= time_end_list: return None # если время вышло
  #print(remain_list, '\n') # технический вывод

  # заём времени
  if remain_list[5] < 0: remain_list[4] -= 1; remain_list[5] += 60
  if remain_list[4] < 0: remain_list[3] -= 1; remain_list[4] += 60
  if remain_list[3] < 0: remain_list[2] -= 1; remain_list[3] += 24
  if remain_list[2] < 0: remain_list[1] -= 1; remain_list[2] += days_in_prev_month(int(time_end_list[0]), int(time_end_list[1]))[1]
  if remain_list[1] < 0: remain_list[0] -= 1; remain_list[1] += 12 

  def with_only_days(): # только время и дни считает 

    cur_years, cur_months = int(time_now_list[0]), int(time_now_list[1])

    for month in range(int(remain_list[1])):
      remain_list[2] += check_days_in_month_and_year(int(time_now_list[0]), int(time_now_list[1]))[1]
      cur_years += 1
      if cur_months > 12:
        cur_months = 1; cur_years += 1
    
    for year in range(int(remain_list[0])):
      remain_list[2] += check_days_in_month_and_year(int(time_now_list[0])+ year + 1, int(time_now_list[1]))[0]

    return True

  if format_number == 1: with_only_days()

  years =   remain_list[0] # пока нужно
  months =  remain_list[1]
  days =    remain_list[2]
  hours =   remain_list[3]
  minutes = remain_list[4]
  seconds = remain_list[5]

  '''
  if remain_list[0] < 10:   years = f"0{remain_list[0]}" # нули прибавляем чтобы красива была 
  if remain_list[1] < 10:  months = f"0{remain_list[1]}"
  if remain_list[2] < 10:    days = f"0{remain_list[2]}"
  if remain_list[3] < 10:   hours = f"0{remain_list[3]}"
  if remain_list[4] < 10: minutes = f"0{remain_list[4]}"  решил пока возвращать сырые числа, так удобнее
  if remain_list[5] < 10: seconds = f"0{remain_list[5]}"  '''
  

  return [years, months, days, hours, minutes, seconds]

#print(calculation("2029-11-08 10:00:00", 0))