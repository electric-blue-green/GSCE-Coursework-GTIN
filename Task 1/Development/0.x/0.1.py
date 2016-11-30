## GITN-8 Task by Thomas Bass
import math

def start():
  print('GTIN-8 Task by Thomas Bass')
  print('A453 Task 1')
  ask()

def ask():
  ask = input('Press [c] to calculate the 8th GTIN Number from 7 numbers. \nPress [v] to vertify an 8 digit GTIN Number \n')
  if ask == 'c' or ask == 'C':
    check7()
  elif ask == 'v' or ask == 'V':
    check8()
  else:
    print('Error: Please enter either \'c\' or \'v\' ')
    ask()  
#################################### 7 digit CALCULATE ####################################
def check7():
  gtin7 = input('Enter the 7 digit Book Number: ')
  try:
           val = int(gtin7)
  except ValueError:
        print("Error: Only Numbers are allowed.")
        check7()
  checklen7(gtin7)

def checklen7(gtin7):
  if len(gtin7) == 7:
      multiply7(gtin7)
  else:
      print('Error: Only 7 digits are allowed')
      check7()

def multiply7(gtin7):
  multiplier = 3
  total = 0
  for counter in range(0, 7, 2):
    convert3 = int(gtin7[counter])
    total = total + (convert3*multiplier)
    if counter == 6:
      calculate7(total, gtin7)
    else:
      multiplier = 1
      convert1 = int(gtin7[counter+1])
      total = total + (convert1*multiplier)
      multiplier = 3

def calculate7(total, gtin7):
  rounded = (int(math.ceil(total / 10.0)) * 10)
  result = (rounded - total)
  print('Final Check Digit = ', result)
  print('Whole GTIN-8 Number = ', gtin7,result)
  
#################################### 8 digit VERIFY ####################################  
def check8():
  gtin8 = input('Enter the 8 digit GTIN: ')
  try:
           val = int(gtin8)
  except ValueError:
        print("Error: Only Numbers are allowed.")
        check8()
  checklen8(gtin8)

def checklen8(gtin8):
  if len(gtin8) == 8:
      multiply8(gtin8)
  else:
      print('Error: Only 8 digits are allowed')
      check8()

def multiply8(gtin8):
  multiplier = 3
  total = 0
  for counter in range(0, 7, 2):
    convert3 = int(gtin8[counter])
    total = total + (convert3*multiplier)
    if counter == 6:
      calculate8(total, gtin8)
    else:
      multiplier = 1
      convert1 = int(gtin8[counter+1])
      total = total + (convert1*multiplier)
      multiplier = 3

def calculate8(total, gtin8):
  checkdig = int(gtin8[7])
  rounded = (int(math.ceil(total / 10.0)) * 10)
  result = (rounded - total)
  print('Final Check Digit = ', result)
  print('Checkdigit = ', checkdig)
  if checkdig == result:
    print('Valid Number')
  else:
    print('Invalid Number')
  park()

def park():
  while True:
    a = input
    
start()
