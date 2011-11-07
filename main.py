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
    print result


##
# Sub-program to help the user find a product.
#
# @param filter_str String containing a filter for the SQL query.
#
# @return FIXME
def search(filter_str):
    conn   = sqlite3.connect(DB)   
    cursor = conn.cursor()
    cursor.execute("select * from product,category where product.name like '%"
                 + filter_str + "%' or category.name like '%"
                 + filter_str + "%' order by category.name,product.name asc")
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
    print "Items in the cart: " + str(len(items)) + "\n"

    option = get_menu_option(['find_product', 'quit'])

    if option == ERROR_OPTION_DOES_NOT_EXIST:
        print "\nWrong option.\n"
    else:
        print "\nCallback to execute: " + option

    return option




# main program
opt = ""
while 1 is 1:
    # show the main menu and get an option from the user
    opt = main_menu()

    # if the option did not exist in the menu, print the menu again
    if opt == ERROR_OPTION_DOES_NOT_EXIST:
        continue

    # load the callback associated with the given option
    self_module = sys.modules[__name__]
    getattr(self_module, opt)()
