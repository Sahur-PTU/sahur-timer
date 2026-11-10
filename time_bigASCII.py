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
    [ " __ ",
      " __|",
      " __|" ],
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
      "  _|",
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
    [ "  __ ",
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
    [ "  __",
      " /__",
      " __/" ],
    [ "  __",
      " /_ ",
      "/__/" ],
    [ " ___",
      "  _/",
      "  / " ],
    [ "  __ ",
      " /__/",
      "/__/ " ],
    [ "  ___",
      " /__/",
      " __/ " ],
      
    [ "   ",
      " - ",
      "-  " ],

    [ "   ",
      "   ",
      " _ " ]
  ]

split_time = ['0','0','1',  '3','4',  '2','7', '1','8']

f_output = [0,0,0,0,0,0,0,0,0,0]

digits = digits_2

def calculation(vew_time): # присваивания под-списков к цифрам

  split_time[0] = vew_time[0][0]
  split_time[1] = vew_time[0][1]
  split_time[2] = vew_time[0][2]

  split_time[3] = vew_time[1][0]
  split_time[4] = vew_time[1][1]

  split_time[5] = vew_time[2][0]
  split_time[6] = vew_time[2][1]

  split_time[7] = vew_time[3][0]
  split_time[8] = vew_time[3][1]


def output(vew_time):
    get_calculation = calculation(vew_time)

    for calc_digit in range(9):
        f_output[calc_digit] = digits[int(split_time[calc_digit])]

    LINE_1 = f"{f_output[0][0]}{f_output[1][0]}{f_output[2][0]}   {f_output[3][0]}{f_output[4][0]}{digits[10][0]}{f_output[5][0]}{f_output[6][0]}{digits[10][0]}{f_output[7][0]}{f_output[8][0]}\033[K"
    LINE_2 = f"{f_output[0][1]}{f_output[1][1]}{f_output[2][1]}   {f_output[3][1]}{f_output[4][1]}{digits[10][1]}{f_output[5][1]}{f_output[6][1]}{digits[10][1]}{f_output[7][1]}{f_output[8][1]}\033[K"
    LINE_3 = f"{f_output[0][2]}{f_output[1][2]}{f_output[2][2]}   {f_output[3][2]}{f_output[4][2]}{digits[10][2]}{f_output[5][2]}{f_output[6][2]}{digits[10][2]}{f_output[7][2]}{f_output[8][2]}\033[K"
    
    print(LINE_1)
    print(LINE_2)
    print(LINE_3, end="", flush=True)
    print("\r\033[2F", end="", flush=True)

import time_calculator


def main(input_time):
    #result = time_calculator.calculation(input_time, 1)
    if len(input_time[0]) < 3: input_time[0] = f"0{input_time[2]}"
    #print(input_time)
    output(input_time)


if __name__ == "__main__":
  while True:
    main(['000', '00','00','00'])
    time.sleep(1)



'''
('001','02','23','30')
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