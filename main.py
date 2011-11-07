#!/usr/bin/python
# Valeriy Volodenkov, Eva Rio, Claudio M. Camacho
# T-121.5300 User Interface Construction
# Aalto University, School of Science
import sys
import sqlite3

ERROR_OPTION_DOES_NOT_EXIST = 991
DB = "products.db"



# keep the number of items in the current cart
items = [ ]
shopping_cart = { }
#goods fetched by search query
temp_goods_list = []


# list of actions
actions = {
    'add_item'     : "Add item",
    'edit_item'    : "Edit item",
    'remove_item'  : "Remove item",
    'checkout'     : "Check out",
    'empty_cart'   : "Empty cart",
    'find_product' : "Find products",
    'quit'         : "Quit" }



##
# Exit the program.
def quit():
    print "\nGoodbye!"
    exit()



##
# Sub-program to help the user find a product.
def find_product():
    print "\n"
    filter_str = raw_input("Enter a product name or description: ")
    result = search(filter_str)
    if result.count > 0:
        global temp_goods_list
        temp_goods_list = result
        print result


##
# Sub-program to help the user find a product.
#
# @param filter_str String containing a filter for the SQL query.
#
# @return a list of tuples with the products that match the filter_str.
def search(filter_str):
    conn   = sqlite3.connect(DB)   
    cursor = conn.cursor()

    # first find all products inside a related category
    cursor.execute("select code from category where name like '%"
                 + filter_str + "%'")
    cats = [ ]
    for c in cursor.fetchall():
        cats.append(str(c[0]))
    categories = ', '.join(cats)
    cursor.execute("select code,name from product where category in ("
                 + categories + ") or name like '%" 
                 + filter_str + "%' order by name asc")
    return cursor.fetchall()



##
# Display a list of options and return the selected option.
#
# @return the name of the callback to execute.
def get_menu_option(options):
    count = 1
    for o in options:
        print str(count) + ". " + actions[o]
        count += 1

    # sanitize input
    try:
        opt = int(raw_input("Your choice: "));
    except:
        opt = 0
    if opt > len(options) or opt < 1:
        return ERROR_OPTION_DOES_NOT_EXIST
    return options[opt - 1];



##
# Display the initial main menu with the major options to the user.
def main_menu():
    #not sure what are items, added shopping cart
    #print "Items in the cart: " + str(len(items)) + "\n"
    print "Items in the cart: " + str(len(shopping_cart)) + "\n"
    # looks messy
    # if we have any item found we can add it
    option_list = []
    if(len(temp_goods_list) > 0):
        option_list = ['add_item', 'quit']
    else:
        option_list = ['find_product', 'quit']
    if (len(shopping_cart) > 0):
        print "!!!!!something is in the cart!!!!!!"
        option_list.extend (['edit_item','checkout','empty_cart'])
    option = get_menu_option(option_list)
    return option

##
# ToDo:Check code before adding
def add_item():
    print "Enter item's code to add it to the cart"
    for item in temp_goods_list:
        print str(item[0]) + ". " + item[1]
    print "\n"
    code = -1
    try:
        code = int(raw_input("Your choice"));
        add_to_cart(code)
    except:
        code = -1
##
# Add item or increase number of item by adding it
def add_to_cart(code):
    try:
        shopping_cart[str(code)] += 1
    #    count = shopping_cart[str(code)]
    #if count >= 0:
    except:
        shopping_cart[str(code)] = 1

##
# Just showing shopping list for now
def checkout():
    print "Here is you shopping cart"
    print shopping_cart

    #tem in shopping_cart:
        #print [x[1] for x in temp_goods_list if x[0]==item]
        #temp_goods_list[item]

    #We need to store items' names somewhere
    del temp_goods_list[:]


def edit_item():
    print "editing..."

def empty_cart():
     shopping_cart.clear()
     del temp_goods_list[:]

# main program
opt = ""
while 1 is 1:
    # show the main menu and get an option from the user
    opt = main_menu()

    # if the option did not exist in the menu, print the menu again
    if opt == ERROR_OPTION_DOES_NOT_EXIST:
        print "\nWrong option.\n"
        continue

    # load the callback associated with the given option
    self_module = sys.modules[__name__]
    getattr(self_module, opt)()
