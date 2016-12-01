__authors__ = ['Thomas Bass']
##    Candidate Number 4869  |  Centre Number 52423
##   TASK 2  ##
import sqlite3 as lite                                                          ## Imports libraries
import random
import math
currentOrder = []                                                               ## Define currentOrder as an array
con = lite.connect('dbuse.db')                                                  ## connects to Database
cur = con.cursor()                                                              ## SQLite
def verify(con, cur, currentOrder):                                             ## Define verify
  var = input('Enter GTIN for the product you wish to purchase:\n> ')           ## input 'var'
  if len(var) == 8 and var.isnumeric() == True:                                 ## If 'var' = 8 and is numerical
    findStock(con, cur, currentOrder, var)                                      ## Call findStock
else:                                                                           ## Else
    print('Enter a 8 digit number')                                             ## Print error
    verify(con, cur, currentOrder)                                              ## call verify

def findStock(con, cur, currentOrder, var):                                     ## Define findStock
  cur.execute('SELECT * FROM Inventory WHERE GTIN = ?', (var,))                 ## excutes
  results = cur.fetchall()                                                      ## collects results from SQL
  con.commit()                                                                  ## Commit .db-journal
  if results == []:                                                             ## If resutls array is empty
    print('No product found. Please try again')                                 ## Print no results found
    verify(con, cur, currentOrder)                                              ## Call verify
  print('Product Found!')                                                       ## Print product Found
  for product in results:                                                       ## Loop for products in resutls
    if product[2] == '':                                                        ## If Product [2] is empty
      sizeName = ''                                                             ## Product [2] is empty
    elif product[2] == 'Small' or product[2] == 'Medium' or product[2] == 'Large':
      sizeName = product[2]                                                     ## If Product [2] is small/medimm/large sizeName = product[2]
    else:
      sizeNameRaw = product[2], 'ml'                                            ## sizeNameRaw = product[2]
      sizeName = "".join(sizeNameRaw)                                           ## sizeName = sizeNameRaw join''
    print('  Name: ', sizeName, product[1], '\n  Price: ', product[3],'
    '\n  Stock Available: ', product[4])
    enterOrder(sizeName, product, var, results, currentOrder, cur, con)         ## Call enterOrder

def enterOrder(sizeName, product, var, results, currentOrder, cur, con):        ## Define enterOrder
  QtyToOrder = input('----------\nEnter Quantity to order:\n>')                 ## Input QtyToOrder
  if QtyToOrder.isnumeric() == False:                                           ## If QtyToOrder is not numerical
    print('Enter a valid Number')                                               ## Error
    enterOrder(sizeName, product, var, results, currentOrder, cur, con)         ## Call enterOrder
elif int(QtyToOrder) > int(product[4]):                                         ## Elif QtyToOrder > product[4]
    print('Error: Not enough stock. Please order', product[4], 'or less')       ## Print 
    enterOrder(sizeName, product, var, results, currentOrder, con, cur)
  elif int(QtyToOrder) < 1:
    print('You can\'t order less than 1. Try again')
    enterOrder(sizeName, product, var, results, currentOrder, con, cur)
  else:
    print('Adding to order...')
    NewStockAvab = 0
    costOfOrder = float(product[3])*int(QtyToOrder)
    currentOrderAddRaw = str(QtyToOrder), ' x ', str(sizeName), ' ', str(product[1]), ' (GTIN: ', str(product[0]), ') @ £',
    //str(product[3]), ' = £', str(costOfOrder)
    currentOrderAdd = "".join(currentOrderAddRaw)
    print('Added to order!')
    print('Updating Stock Levels...')
    QtyInt = int(QtyToOrder)
    NewStockAvab = str((int(product[4])) - QtyInt)
    sql = ("UPDATE INVENTORY SET STOCKAVAB = '"+NewStockAvab+"' WHERE GTIN LIKE '"+product[0]+"'")
    try:
      cur.execute(sql)
      con.commit()
      print('Updated')
    except:
      print('Error: Inventory Update failed to commit.')
      currentOrder.append(currentOrderAdd+' [CANCELLED]')
      print('\n\nPLEASE ENTER \'100\' TO ESCAPE ERROR\n\n')
      enterOrder(sizeName, product, var, results, currentOrder, cur, con)
    currentOrder.append(currentOrderAdd)
    again = input('Order another item? [Y/N]:\n>')
    if again == 'Y' or again == 'y':
      verify(con, cur, currentOrder)
    if again == 'N' or again == 'n':
      print('Order finished!')
      print('Receipt:')
      for order in currentOrder:
        print(order)

def ask(cur, con, currentOrder):
  askQuery = input('Press [s] to search for a product\'s GTIN number:\n> ')
  if askQuery == 's' or askQuery == 'S':
    verify(con, cur, currentOrder)
  else:
    print('Invalid Choice')
    ask(cur, con, currentOrder)

ask(cur, con, currentOrder)     ## Calls first func
