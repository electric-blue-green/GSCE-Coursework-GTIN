__authors__ = ['Thomas Bass']
##   Candidate Number 4869  |  Centre Number 52423
##   TASK 2
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
  else:                                                                         ## Else
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
    print('  Name: ', sizeName, product[1], '\n  Price: ', product[3],
      '\n  Stock Available: ', product[4])
    enterOrder(sizeName, product, var, results, currentOrder, cur, con)         ## Call enterOrder

def enterOrder(sizeName, product, var, results, currentOrder, cur, con):        ## Define enterOrder
  QtyToOrder = input('----------\nEnter Quantity to order:\n>')                 ## Input QtyToOrder
  if QtyToOrder.isnumeric() == False:                                           ## If QtyToOrder is not numerical
    print('Enter a valid Number')                                               ## Error
    enterOrder(sizeName, product, var, results, currentOrder, cur, con)         ## Call enterOrder
  elif int(QtyToOrder) > int(product[4]):                                       ## Elif QtyToOrder > product[4]
    print('Error: Not enough stock. Please order', product[4], 'or less')       ## Print
    enterOrder(sizeName, product, var, results, currentOrder, con, cur)         ## Call enterOrder
  elif int(QtyToOrder) < 1:                                                     ## Elif QtyToOrder < 1
    print('You can\'t order less than 1. Try again')                            ## Print error
    enterOrder(sizeName, product, var, results, currentOrder, con, cur)         ## Call enterOrder
  else:                                                                         ## else
    print('Adding to order...')                                                 ## Print addint to order
    NewStockAvab = 0                                                            ## Set NewStockAvab = 0
    costOfOrder = float(product[3])*int(QtyToOrder)                             ## costOfOrder = product[3]*QtyToOrder
    currentOrderAddRaw = str(QtyToOrder), ' x ', str(sizeName), ' ', str(product[1]), ' (GTIN: ', str(product[0]), ') @ £', str(product[3]), ' = £', str(costOfOrder)
    currentOrderAdd = "".join(currentOrderAddRaw)                               ## currentOrderAdd = costOfOrder join ''
    print('Added to order!')                                                    ## Print adding to order
    print('Updating Stock Levels...')                                           ## Print updating stock levels
    QtyInt = int(QtyToOrder)                                                    ## QtyInt = QtyToOrder
    NewStockAvab = str((int(product[4])) - QtyInt)                              ## NewStockAvab = product[4] - QtyInt
    sql = ("UPDATE INVENTORY SET STOCKAVAB = '"+NewStockAvab+"' WHERE GTIN LIKE '"+product[0]+"'")                      ## SQL query
    try:                                                                        ## try
      cur.execute(sql)                                                          ## Execute SQL
      con.commit()                                                              ## Commit .db-journal
      print('Updated')                                                          ## Print 'updated'
    except:                                                                     ## SQL Rejection
      print('Error: Inventory Update failed to commit.')                        ## Print Error
      currentOrder.append(currentOrderAdd+' [CANCELLED]')                       ## append order cancellation
      print('\n\nPLEASE ENTER \'100\' TO ESCAPE ERROR\n\n')                     ## Print error escape message
      enterOrder(sizeName, product, var, results, currentOrder, cur, con)       ## Call enterOrder
    currentOrder.append(currentOrderAdd)                                        ## Call currentOrder
    again = input('Order another item? [Y/N]:\n>')                              ## Input 'again'
    if again == 'Y' or again == 'y':                                            ## If again = 'Y'
      verify(con, cur, currentOrder)                                            ## Call verify
    if again == 'N' or again == 'n':                                            ## If ayain = 'n'
      print('Order finished!')                                                  ## Print order complete
      print('Receipt:')                                                         ## Print receipt
      for order in currentOrder:                                                ## For orders in currentOrder
        print(order)                                                            ## Print 'order'

def ask(cur, con, currentOrder):                                                ## Defien ask
  askQuery = input('Press [s] to search for a product\'s GTIN number:\n> ')     ## askQuery = input 'S'
  if askQuery == 's' or askQuery == 'S':                                        ## If askQuery
    verify(con, cur, currentOrder)                                              ## Call verify
  else:                                                                         ## else
    print('Invalid Choice')                                                     ## Print invalid choice
    ask(cur, con, currentOrder)                                                 ## Call ask

ask(cur, con, currentOrder)                                                     ## Call ask