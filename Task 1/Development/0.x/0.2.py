import math             ## Imports functopns
import sys
print('GCSE Controlled Assesment A453\nThomas Bass 4869\nTask 1')
def start():        ## Main process
  ask = input('Press [c] to calculate the 8th GTIN Number from 7 numbers. \nPress [v] to vertify an 8 digit GTIN Number \n')
  if ask == 'c' or ask == 'C':
    gtin = 0
    length = 7
    check(length)
  elif ask == 'v' or ask == 'V':
    gtin = 0
    length = 8
    check(length)
  else:
    print('Error: Please enter either \'c\' or \'v\' ')
    start()  
def check(length):
  print('Enter the', length, 'digit GTIN number')
  gtin = input(': ')
  if len(gtin) == length and gtin.isnumeric() == True:
    total = 0
    for counter in range(0, 7, 2):
      total = total + ((int(gtin[counter]))*3)
      if counter == 6:
        checkdig = int(gtin[length-1])
        rounded = (int(math.ceil(total / 10.0)) * 10)
        result = (rounded - total)
        if length == 7:
          print('Final Check Digit = ', result)
          print('Whole GTIN-8 Number = ', gtin,result)
          park()
        else:
          if checkdig == result:
            print(gtin, 'is a Valid Number')
          else:
            print(gtin, 'is an Invalid Number')
          park()
      else:
        total = total + ((int(gtin[counter+1]))*1)
  else:
    print('Error: Only', length, 'numbers are allowed. Try again ')
    check(length)
def park():
  again = input('Do you want to calculate or verify another number? \n[n] No [y] Yes: ')
  if again == 'n' or again == 'N':
    sys.exit()
  elif again == 'y' or again == 'Y':
    start()
start()
