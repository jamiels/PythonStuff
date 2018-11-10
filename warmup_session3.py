menu_options = {'hamburgers':1.99,
        'pizza':1.5,
        'fries':1.25,
        'soda':1}
        
def display_menu():
    for k,v in menu_options.items():
        print(k,'is',v) 
    choice = int(input('Which one?'))
    return choice 
     

shopping_list={'hamburgers':0,
                'pizza':0,
                'fries':0,
                'soda':0}

MENU_OPTION_EXIT = 5

user_active =True
while user_active:
    choice = display_menu()
    if choice < MENU_OPTION_EXIT:
        qty = int(input('How many?'))
        keys=list(menu_options)[qty-1]
        shopping_list[keys]=shopping_list[keys]+qty
        print(shopping_list)

    if choice == MENU_OPTION_EXIT:
        user_active = False

print('bye bye')  