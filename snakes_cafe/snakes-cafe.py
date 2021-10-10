print('''**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
''')

"""create a menu list inside it type of the food 
and make  a dictionary of type of the food assign into the type of dishes with init value zero 
init value represents how many orders we take for the same dishes 
"""
Appetizers={
'Wings':0,
'Cookies':0,
'Spring Rolls':0}
Entrees={
'Salmon':0,
'Steak':0,
'Meat Tornado':0,
'A Literal Garden':0}
Desserts={
'Ice Cream':0,
'Cake':0,
'Pie':0,}
Drinks={
'Coffee':0,
'Tea':0,
'Unicorn Tears':0}
menu = [Appetizers ,Entrees,Desserts,Drinks ]

""" assigin variable  how will be  responsible if the item the found in the list or no  
 check if the user not write quit then make a for loop looping through the list then dictionary"""

print('''
***********************************
** What would you like to order? **
***********************************
''')
response = input('>').strip().capitalize() 
while response != 'Quit':
    found=True
    for order in menu:
       for order_item in order.keys():
           if order_item == response:
                 found = False
                 order[response]+=1
                 value=order[response]
                 res=[response]
                 print(f"** {value} order of {response} have been added to your meal **")
    if found:  
        print(f"** {response}  not found on  the menu  **")
    response=input('order secend item >').strip().capitalize()
print("Thank you for your visit")