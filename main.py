#!/usr/bin/python
# TODO: headers

# keep the number of items in the current cart
no_items = 0

# list of actions
actions = 
{
    'add_item'    : "Add item",
    'edit_item'   : "Edit item",
    'remove_item' : "Remove item",
    'checkout'    : "Check out",
    'empty_cart'  : "Empty cart",
    'search'      : "Search product",
    'quit'        : "Quit"
}





##
# Exit the program.
def quit():
    exit()


##
# Display a list of options and return the selected option.
def get_menu_option(options):
    count = 1
    # TODO: dictionary with count+options
    for o in options:
        print count + ". " + actions[o]


##
# Display the initial main menu with the major options to the user.
def main_menu():
    print "Items in the cart: " + no_items
    print "\n"
    option = get_menu_option('search', 'quit')





# main program
main_menu()
