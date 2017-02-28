__authors__ = ['Thomas Bass']
##   Candidate Number 4869  |  Centre Number 52423
##   TASK 2
import sqlite3 as lite
import random
import math
currentOrder = []
con = lite.connect('dbuse.db')
cur = con.cursor()
def verify(con, cur, currentOrder):
  var = input('Enter GTIN for the product you wish to purchase:\n> ')
  if len(var) == 8 and var.isnumeric() == True:
    findStock(con, cur, currentOrder, var)
  else:
    print('Enter a 8 digit number')
    verify(con, cur, currentOrder)

def findStock(con, cur, currentOrder, var):
  cur.execute('SELECT * FROM Inventory WHERE GTIN = ?', (var,))
  results = cur.fetchall()
  con.commit()
  if results == []:
    print('No product found. Please try again')
    verify(con, cur, currentOrder)
  print('Product Found!')
  for product in results:
    if product[2] == '':
      sizeName = ''
    elif product[2] == 'Small' or product[2] == 'Medium' or product[2] == 'Large':
      sizeName = product[2]
    else:
      sizeNameRaw = product[2], 'ml'
      sizeName = "".join(sizeNameRaw)
    print('  Name: ', sizeName, product[1], '\n  Price: ', product[3],'
    '\n  Stock Available: ', product[4])
    enterOrder(sizeName, product, var, results, currentOrder, cur, con)

def enterOrder(sizeName, product, var, results, currentOrder, cur, con):
  QtyToOrder = input('----------\nEnter Quantity to order:\n>')
  if QtyToOrder.isnumeric() == False:
    print('Enter a valid Number')
    enterOrder(sizeName, product, var, results, currentOrder, cur, con)
  elif int(QtyToOrder) > int(product[4]):
    print('Error: Not enough stock. Please order', product[4], 'or less')
    enterOrder(sizeName, product, var, results, currentOrder, con, cur)
  elif int(QtyToOrder) < 1:
    print('You can\'t order less than 1. Try again')
    enterOrder(sizeName, product, var, results, currentOrder, con, cur)
  else:
    print('Adding to order...')
    NewStockAvab = 0
    costOfOrder = float(product[3])*int(QtyToOrder)
    currentOrderAddRaw = str(QtyToOrder), ' x ', str(sizeName), ' ', str(product[1]), ' (GTIN: ', str(product[0]), ') @ £', str(product[3]), ' = £', str(costOfOrder)
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
      currentOrder.append(currentOrderAdd+' [CANCELLED
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

ask(cur, con, currentOrder)
