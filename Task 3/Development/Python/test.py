added = ['qty', 'add']
def go(added):
  add = input('Enter addition here: ')
  qty = input('Enter value here: ')
  added.append([0](qty))
  again = input('Go again?')
  print(added)
  if again == 'y':
    go(added)

go(added)
