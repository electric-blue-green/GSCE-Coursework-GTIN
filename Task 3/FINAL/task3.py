__authors__ = ['Thomas Bass']
##    TASK 3   ##
import sqlite3 as lite                                                                                                        ## Imports libraries
import random
import math
import sys
stockOrder = []
con = lite.connect('dbuse.db')                                                                                                ## connects to DBase
cur = con.cursor()
def findStock(con, cur, stockOrder):
  slq1 = 'SELECT * FROM Inventory WHERE StockAvab != TargetStock'                                                             ## selects low stock from DBase
  cur.execute(slq1)                                                                                                           ## excesutes
  results = cur.fetchall()                                                                                                    ## collects
  orderList = []
  if str(results):
    print('Stock is all up to date!')
    park()
  for product in results:
    toOrder = int(int(product[5]) - int(product[4]))                                                                          ## math for how many to order
    print('Low stock! Order', toOrder, 'x', product[1], 'more to fill stock')                                           ## message
    if product[2] == '':
      sizeName = ''
    elif product[2] == 'Small' or product[2] == 'Medium' or product[2] == 'Large':                                      ## Elif 
      sizeName = product[2]                                                                                             ## sizeName = product[2]
  else:                                                                                                                 ## Else
      sizeNameRaw = product[2], 'ml'                                                                                    ## sizeNameRaw = product[2] + ml
      sizeName = "".join(sizeNameRaw)                                                                                   ## sizeName = join sizeNameRaw ''
    stockOrderAddRaw = (str(toOrder), ' x ', str(sizeName), ' ', str(product[1]), ' (GTIN: ', str(product[0]), ')')     ## creates order
    stockOrderAdd = "".join(stockOrderAddRaw)
    stockOrder.append(stockOrderAdd)
    orderList.append(product[0])
    print('       Added to order form')
  print('\n~~~~~~~~~Stock Order Form~~~~~~~~~')
  for i in stockOrder:
    print(i)                                                                                     ## prints order
  updateContinue = input('Is the order complete? [Y/N]\n>')
  if updateContinue == 'Y' or 'y':
    updateStock(con, cur, stockOrder, toOrder, orderList)
  else:
    findStock(con, cur, stockOrder)

def updateStock(con, cur, stockOrder, toOrder, orderList):
  ##print(orderList)
  print('Updating Database...')
  for productUpdate in orderList:
    sql2 = "UPDATE INVENTORY SET STOCKAVAB = TARGETSTOCK WHERE GTIN LIKE '"+productUpdate+"'"
    try:
      cur.execute(sql2)
      con.commit()
      print('Complete #', productUpdate)
    except:
      print('An exception occured.')
      findStock(con, cur, stockOrder)

def park():
  sys.exit()

ask = input('Press [s] to scan inventory stock levels\n> ')
if ask == 's' or ask == 'S':
  findStock(con, cur, stockOrder)
