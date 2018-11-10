def display_menu():
    menu_options=['burgers1','pizza2','fried chicken3','exit4']
    print(menu_options)

def fastfood_menu():
  shopping_list=[]

  still_ordering = True
  while still_ordering:
    display_menu()
    user_order=int(input('plz input a number 1,2,3or4'))
    shopping_list.append(menu_options[user_order-1])
  print(shopping_list)

fastfood_menu()