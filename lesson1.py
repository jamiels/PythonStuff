def fastfood_menu():
  menu_options=['burgers1','pizza2','fried chicken3','exit4']
  shopping_list=[]
  user_order = -1
  while user_order<4:
    print(menu_options)
    user_order=int(input('plz input a number 1,2,3or4'))
    shopping_list.append(menu_options[user_order-1])
  else:
    print(shopping_list)

fastfood_menu()