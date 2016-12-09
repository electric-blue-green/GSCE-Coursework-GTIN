import math                                                                     ## Imports Math and Sys librarys
import sys
print('GCSE Controlled Assesment A453\nThomas Bass 4869\nTask 1')
def start():                                                                    ## Defines 'start'
  ask = input('Press [c] to calculate the 8th digit from 7\n
  'Press [v] to vertify an 8 digit GTIN Number \n')                             ## Ask the user if they want to verify or calculate
  if ask == 'c' or ask == 'C':                                                  ## If user chooses to calculate
    length = 7                                                                  ## 'length' is 7
  elif ask == 'v' or ask == 'V':                                                ## If user chooses to verify
    length = 8                                                                  ## 'length' is 8
  else:                                                                         ## else
    print('Error: Please enter either \'c\' or \'v\' ')                         ## Error message
    start()                                                                     ## Return to 'start'
  check(length)                                                                 ## Call 'check' function
def check(length):                                                              ## Define 'check' function
  print('Enter the', length, 'digit GTIN number')                               ## Ask the user to input the GTIN
  gtin = input(': ')                                                            ## Input 'gtin'
  if len(gtin) == length and gtin.isnumeric() == True:                          ## If the length of 'gtin' is equal to 'length' and 'gtin' is numeric
    total = 0                                                                   ## 'total' is 0
    for counter in range(0, 7, 2):                                              ## For 7 iterations, stepping 'counter' by 2
      total = total + ((int(gtin[counter]))*3)                                  ## 'total' is 'total' plus 'gtin' position 'counter' times 3
      if counter == 6:                                                          ## If 'counter' is 6
        checkdig = int(gtin[length-1])                                          ## 'checkdig' is 'gtin' position 'length' -1
        rounded = (int(math.ceil(total / 10.0)) * 10)                           ## 'rounded' is ceil of 'total' /10.0 * 10 (rounded up to multiple of 10)
        result = (rounded - total)                                              ## 'result' is 'rounded' - 'total'
        if length == 7:                                                         ## If 'length' is 7
          print('Final Check Digit = ', result)                                 ## Print 'result'
          print('Whole GTIN-8 Number = ', gtin,result)                          ## Print 'gtin'+'result'
          park()                                                                ## Call 'park' function
        else:                                                                   ## Else
          if checkdig == result: print(gtin, 'is a Valid Number')               ## If 'checkdig' equals 'result': GTIN is valid
          else: print(gtin, 'is an Invalid Number')                             ## Else: GTIN is invalid
          park()                                                                ## Call 'park' function
      else:                                                                     ## Else
        total = total + ((int(gtin[counter+1]))*1)                              ## 'total' is 'total' plus 'gtin' position 'counter'
  else:                                                                         ## Else
    print('Error: Only', length, 'numbers are allowed. Try again ')             ## Print error message
    check(length)                                                               ## Call 'check' function
def park():                                                                     ## Define 'park' function
  again = input('Do you want to calculate or verify another number?'
  '\n[n] No [y] Yes: ')                                                         ## Ask the user to go again
  if again == 'n' or again == 'N':                                              ## If No:
    sys.exit()                                                                  ## Close program
  elif again == 'y' or again == 'Y':                                            ## If Yes:
    start()                                                                     ## Call 'start' function
start()                                                                         ## Call 'start' function



