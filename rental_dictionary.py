rentals = {
 '1a':3000,
 '1b':2000,
 '2b':3050,
 '3d':2000,
 '4c':3120,
}
MENU_VIEW = 1
MENU_ADD = 2
MENU_DELETE = 3
MENU_EXIT = 4

menu = ('View','Add','Delete','Exit')
user_active = True
while user_active:
  for n in menu:
    print(n)
  choice = int(input('pick one 1-4'))
  if choice==MENU_ADD:
    apt_name = input('name of apartment?')
    rent = int(input('rent of apartment'))
    rentals.update({apt_name:rent})
  elif choice==MENU_VIEW:
    for k,v in rentals.items():
      print(k,'is $',v)
  elif choice==MENU_EXIT:
    user_active = False
  elif choice==MENU_DELETE:
    apt_to_delete = input('what apartment?')
    del rentals[apt_to_delete]
  

