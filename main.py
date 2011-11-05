#!/usr/bin/python
# Valeriy Volodenkov, Eva Rio, Claudio M. Camacho
# T-121.5300 User Interface Construction
# Aalto University, School of Science
import sys



# keep the number of items in the current cart
no_items = 0



# list of actions
actions = {
    'add_item'    : "Add item",
    'edit_item'   : "Edit item",
    'remove_item' : "Remove item",
    'checkout'    : "Check out",
    'empty_cart'  : "Empty cart",
    'search'      : "Search product",
    'quit'        : "Quit" }





##
# Exit the program.
def quit():
    print "\nGoodbye!"
    exit()


##
# Sub-program to help the user find a product.
def search():
    print "\nsearch() called successfully!"


##
# Display a list of options and return the selected option.
#
# @return the name of the callback to execute.
def get_menu_option(options):
    count = 1
    for o in options:
        print str(count) + ". " + actions[o]
        count += 1

    return options[int(raw_input("Your choice: ")) - 1];


##
# Display the initial main menu with the major options to the user.
def main_menu():
    print "Items in the cart: " + str(no_items) + "\n"

    option = get_menu_option(['search', 'quit'])

    print "\nCallback to execute: " + option
    return option




# main program
opt = ""
while 1 is 1:
    opt = main_menu()
    self_module = sys.modules[__name__]
    getattr(self_module, opt)()
