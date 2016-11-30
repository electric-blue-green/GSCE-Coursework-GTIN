import math, sys, csv, string, os, re
print('GCSE Controlled Assesment A453\nThomas Bass 4869\nTask 2')
database = []
def start(database, orderGtin, orderPos, orderQty, orderName, items):
  print('Reading File...')
  os.getcwd()
  filename = 'task2.csv'
  filepath = os.path.join(os.getcwd(), filename)
  database = []
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      database.append(row)
  find(database, orderGtin, orderPos, orderQty, orderName, items)

  
  

def find(database, orderGtin, orderPos, orderQty, orderName, items):
  print('Enter the GTIN Number of the product you wish to find')
  gtin = input(':')
  for value in database:
    if gtin in value[0]:
      print('Product Found!')
      product = database.index(value)
      name = database[product][1]
      volume = database[product][2]
      price = database[product][3]
      stock = database[product][4]
      if volume.isnumeric() == True:
        full = volume+'ml'
      else:
        full = ''
      print('Product Name =', full, name)
      print(stock, 'in stock')
      print('Enter the quantity you wish to buy')
      qty = input(': ')
      print(qty, full, name, '@', price)
      print('Add to order? Y/N (This can not be un-done)')
      add = input(': ')
      if add == 'y' or add == 'Y':
          orderGtin.append(gtin)
          orderPos.append(product)
          orderQty.append(qty)
          orderName.append(qty+'x'+full+' '+name+' @ £'+price)
          items = items + 1
          print('Current order')
          print(orderName)
          editStock(gtin, product, stock, qty)
          print('Add another item?(Y/N)')
          again = input(': ')
          if again == 'y' or again == 'Y':
            find(database, orderGtin, orderPos, orderQty, orderName, items)
          else:
            print('Final order')
            print(orderName)
            print('Order Shipped!')
      else:
          print('Order Cancled')
          find(database)

def editStock(gtin, product, stock, qty):
  changeTo = int(stock) - int(qty)
  changeTo = str(changeTo)
  data = open("task2.csv").read()
  data = data.split("\n")
  for i, s in enumerate(data):
    data[i] = data[i].split(",")
  data[product][4] = changeTo
  for i, s in enumerate(data):
    data[i] = str(",".join(data[i]))
  data = "\n".join(data)
  o = open("task2.csv","w")
  o.write(data)
  o.close()
  
  
orderGtin = []
orderPos = []
orderQty = []
orderName = []
items = 0
start(database, orderGtin, orderPos, orderQty, orderName, items)
