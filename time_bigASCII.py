import time
# from счётчик import rem_time
#import счётчик

#rem_time = счётчик.rem_time
#print(rem_time)

"""
  __  
 / / 
/_/  
  _    
  /   
_/_ 
  __   
 __/ 
/__  
  __  
 __/
__/ 
 _    
/__/ 
  / 
 __ 
/__  
__/ 
  __ 
 /_   
/__/ 
___ 
  / 
 / 
  ___ 
 /__/ 
/__/ 
 ___
/__/
__/
"""
s = ['0','0',':','0','0',':','0','0']


digits = [
    [ "  __",
      " / /",
      "/_/ " ],
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
    [ " __",
      "/__",
      "__/" ],
    [ "  __",
      " /_ ",
      "/__/" ],
    [ " ___",
      "   /",
      "  / " ],
    [ "  __",
      " /_/",
      "/_/ " ],
    [ " ___",
      "/__/",
      "__/ " ],
      
    [ "  ",
      " -",
      "- " ]
  ]

import os 
os.system('cls')
import random

a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)

s = ['0','1',  '3','4',  '2','7']

final_output = [0,0,0,0,0,0,0,0,0,0]

import datetime 


def calculation():
  a = str(datetime.datetime.now())[11:-7]
  b = a.split(':')

  s[0] = list(b[0])[0]
  s[1] = list(b[0])[1]
  s[2] = list(b[1])[0]
  s[3] = list(b[1])[1]
  s[4] = list(b[2])[0]
  s[5] = list(b[2])[1]

while True:
  try:
    get_calculation = calculation()
    for calc_digit in range(6):
      final_output[calc_digit] = digits[int(s[calc_digit])]
    LINE_1 = f"{final_output[0][0]} {final_output[1][0]}{digits[10][0]} {final_output[2][0]} {final_output[3][0]}{digits[10][0]} {final_output[4][0]} {final_output[5][0]}\033[K"
    LINE_2 = f"{final_output[0][1]} {final_output[1][1]}{digits[10][1]} {final_output[2][1]} {final_output[3][1]}{digits[10][1]} {final_output[4][1]} {final_output[5][1]}\033[K"
    LINE_3 = f"{final_output[0][2]} {final_output[1][2]}{digits[10][2]} {final_output[2][2]} {final_output[3][2]}{digits[10][2]} {final_output[4][2]} {final_output[5][2]}\033[K"
    print(LINE_1)
    print(LINE_2)
    print(LINE_3, end="", flush=True)
    print("\r\033[2F", end="", flush=True)
    time.sleep(1)
  except KeyboardInterrupt: break
 


exit()
print(digits[a][0] + digits[c][0] + digits[b][0])
print(digits[a][1] + digits[c][1] + digits[b][1])
print(digits[a][2] + digits[c][2] + digits[b][2])




'''
if rem_time[0][0] == '0':
    s[0] = ("""
  __  
 / / -
/_/ - """)
if rem_time[0][0] == '1':
    s[0] = ("""
  _    
  /  - 
_/_ - """)
if rem_time[0][0] == '2':
    s[0] = ("""
  __   
 __/ -
/__ - """)
if rem_time[0][0] == '3':
    s[0] = ("""
  __  
 __/ -
__/ - """)
if rem_time[0][0] == '4':
    s[0] = ("""
 _    
/__/ -
  / - """)
if rem_time[0][0] == '5':
    s[0] = ("""
 __ 
/__  - 
__/ - """)
if rem_time[0][0] == '6':
    s[0] = ("""
  __ 
 /_   -
/__/ - """)
if rem_time[0][0] == '7':
    s[0] = ("""
___ 
  / -
 / - """)
if rem_time[0][0] == '8':
    s[0] = ("""
  ___ 
 /__/ - 
/__/ - """)
if rem_time[0][0] == '9':
    s[0] = ("""
  ___ 
 /__/ -
 __/ - """)

'''
