import time
import datetime

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
"""
  __ 
 |  |
 |__|
   _  
  /| 
  _|_
  __  
  __| 
 |__  
  __  
  __| 
  __|  
  _  _ 
  |__| 
     |  
   __  
  |__  
   __| 
   __ 
  |__  
  |__| 
  __
    |
    |
   __  
  |__| 
  |__| 
   __
  |__|
   __|
"""

digits_1 = [
    [ " __ ",
      "|  |",
      "|__|" ],
    [ " _ ",
      "/| ",
      "_|_" ],
    [ " __ ",
      " __|",
      "|__ " ],
    [ "__ ",
      "__|",
      "__|" ],
    [ "_   ",
      "|__|",
      "   |" ],
    [ " __ ",
      "|__ ",
      " __|" ],
    [ " __ ",
      "|__ ",
      "|__|" ],
    [ " __ ",
      "   |",
      "   |" ],
    [ " __ ",
      "|__|",
      "|__|" ],
    [ " __ ",
      "|__|",
      " __|" ],
      
    [ "   ",
      " - ",
      " - " ]
  ]


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

final_output = [0,0,0,0,0,0,0,0,0,0]

digits = digits_2

def calculation():
  time_now = str(datetime.datetime.now())[11:-7]
  b = time_now.split(':')

  split_time_now[0] = list(b[0])[0]
  split_time_now[1] = list(b[0])[1]
  split_time_now[2] = list(b[1])[0]
  split_time_now[3] = list(b[1])[1]
  split_time_now[4] = list(b[2])[0]
  split_time_now[5] = list(b[2])[1]

while True:
  try:
    get_calculation = calculation()
    for calc_digit in range(6):
      final_output[calc_digit] = digits[int(split_time_now[calc_digit])]
    LINE_1 = f"{final_output[0][0]}{final_output[1][0]}{digits[10][0]}{final_output[2][0]}{final_output[3][0]}{digits[10][0]}{final_output[4][0]}{final_output[5][0]}\033[K"
    LINE_2 = f"{final_output[0][1]}{final_output[1][1]}{digits[10][1]}{final_output[2][1]}{final_output[3][1]}{digits[10][1]}{final_output[4][1]}{final_output[5][1]}\033[K"
    LINE_3 = f"{final_output[0][2]}{final_output[1][2]}{digits[10][2]}{final_output[2][2]}{final_output[3][2]}{digits[10][2]}{final_output[4][2]}{final_output[5][2]}\033[K"
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