__authors__ = ['Thomas Bass']
##    TASK 3   ##
import sqlite3 as lite                                                                                                  ## Imports libraries
import random
import math
import sys
stockOrder = []
con = lite.connect('dbuse.db')                                                                                          ## connects to .db
cur = con.cursor()                                                                                                      ## connects to SQL
def findStock(con, cur, stockOrder):                                                                                    ## Define findStock
  slq1 = 'SELECT * FROM Inventory WHERE StockAvab != TargetStock'                                                       ## selects low stock from DBase
  cur.execute(slq1)                                                                                                     ## excesutes
  results = cur.fetchall()                                                                                              ## collects
  orderList = []                                                                                                        ## Define orderList as array
  if str(results):                                                                                                      ## If results are a string
    print('Stock is all up to date!')                                                                                   ## Print stock up to date
    park()                                                                                                              ## Call park
  for product in results:                                                                                               ## For results loop
    toOrder = int(int(product[5]) - int(product[4]))                                                                    ## math for how many to order
    print('Low stock! Order', toOrder, 'x', product[1], 'more to fill stock')                                           ## message
    if product[2] == '':                                                                                                ## If product[2] is empty
      sizeName = ''                                                                                                     ## SizeName = ' '
    elif product[2] == 'Small' or product[2] == 'Medium' or product[2] == 'Large':                                      ## Elif
      sizeName = product[2]                                                                                             ## sizeName = product[2]
  else:                                                                                                                 ## Else
      sizeNameRaw = product[2], 'ml'                                                                                    ## sizeNameRaw = product[2] + ml
      sizeName = "".join(sizeNameRaw)                                                                                   ## sizeName = join sizeNameRaw ''
    stockOrderAddRaw = (str(toOrder), ' x ', str(sizeName), ' ', str(product[1]), ' (GTIN: ', str(product[0]), ')')     ## creates order
    stockOrderAdd = "".join(stockOrderAddRaw)                                                                           ## Join stockOrderAdd ''
    stockOrder.append(stockOrderAdd)                                                                                    ## Append stockOrderAdd to stockOrder
    orderList.append(product[0])                                                                                        ## Append product[0] orderList
    print('       Added to order form')                                                                                 ## Print added to order
  print('\n~~~~~~~~~Stock Order Form~~~~~~~~~')                                                                         ## Print stock order form
  for i in stockOrder:                                                                                                  ## Print stockOrder
    print(i)                                                                                                            ## prints order
  updateContinue = input('Is the order complete? [Y/N]\n>')                                                             ## input updateContinue
  if updateContinue == 'Y' or 'y':                                                                                      ## If updateContinue = 'y' 'Y'
    updateStock(con, cur, stockOrder, toOrder, orderList)                                                               ## Call updateStock
  else:                                                                                                                 ## Else
    findStock(con, cur, stockOrder)                                                                                     ## Call findStock

def updateStock(con, cur, stockOrder, toOrder, orderList):                                                              ## Define updateStock
  ##print(orderList)                                                                                                    ## ##Print order list
  print('Updating Database...')                                                                                         ## Print updating database
  for productUpdate in orderList:                                                                                       ## Loop in orderList
    sql2 = "UPDATE INVENTORY SET STOCKAVAB = TARGETSTOCK WHERE GTIN LIKE '"+productUpdate+"'"                           ## SQL command
    try:                                                                                                                ## try
      cur.execute(sql2)                                                                                                 ## Execute SQL command
      con.commit()                                                                                                      ## Commit .db-journal
      print('Complete #', productUpdate)                                                                                ## Print completed number
    except:                                                                                                             ## Exception
      print('An exception occured.')                                                                                    ## Print exception error
      findStock(con, cur, stockOrder)                                                                                   ## Call findStock

def park():                                                                                                             ## Define stock
  sys.exit()                                                                                                            ## Sys exit

ask = input('Press [s] to scan inventory stock levels\n> ')                                                             ## Ask input
if ask == 's' or ask == 'S':                                                                                            ## If ask = 's'
  findStock(con, cur, stockOrder)
else:
   sys.exit()                                                                                    ## Call findStock
