# This function will be called then assign the contents of the text file 'list.txt' to a list called 'coll'(Collection).
def list_function():
    with open('list.txt', 'r') as file:
        coll = file.read().split()
        return coll


# This function acts as a main menu that will give the user access to each parts of the program in an easy manner.
def main():
    coll = list_function()
    while True:
        try:
            user_input = int(input("----------MAIN MENU----------\n1)Add to list\n2)Search list\n3)Remove from list\n4)Save changes\n5)Cancel changes/Refresh\n6)Print list\n7)Sorting table\n-----------------------------\n>>> "))
            match user_input:
                case 1:
                    add_to_list(coll)
                case 2:
                    search_list(coll)
                case 3:
                    remove_list(coll)
                case 4:
                    save_to_file(coll)
                case 5:
                    print("All changes have been restored! ")
                    main()  # by using recursion with the main() function the list 'coll' will get redefined with 'coll = list_function()' at the start of main(), in other words will replenish the list with the current txt contents.
                case 6:
                    for_print_function(coll)
                    print("\n\n")
                case 7:
                    list_sorting_table(coll)
                case _:
                    print("\nInvalid option, please try again:")
        except ValueError as e:
            print(f"ERROR! {e} has caused an Value error!")
        except Exception as e:
            print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


# This function will ask for user input from the user_function_with_confirm that will then be appended to the end of the list.
def add_to_list(coll):
    while True:
        try:
            for_print_function(coll)
            print("Enter the name of the item you would like to add: ")
            user_input = user_function_with_confirm()
            if user_input is False:
                break
            else:
                coll.append(user_input)  # The data that the user wants to add into the list will be added into the end.
        except Exception as e:
            print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


# This function gives the user the ability to search the list for a specific item.
def search_list(coll):
    while True:
        try:
            for_print_function(coll)
            target = name_or_index_function(coll)
            if target is False:
                break
            print(f"\nItem index| {target}\n Item name| {coll[target]}")
        except ValueError:
            print("ERROR!")
        except Exception as e:
            print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


# This function, like the 'search_list' function will ask the user for an item name and then remove that item from the list.
def remove_list(coll):
    while True:
        try:
            for_print_function(coll)
            target = name_or_index_function(coll)
            if target is False:
                break
            confirm = input(f"\nType '//' to return to main menu:\nAre you sure you want to remove this item?\nItem index| {target}\n Item name| {coll[target]}\nY/N:\n>>> ")
            match confirm.lower():
                case '//':
                    break
                case 'y':
                    del coll[target]
                    print("Item(s) have been removed! ")
                case 'n':
                    print("Changes have not been made! ")
                    continue
                case _:
                    print("ERROR! ")
        except ValueError:
            print("ERROR! That item doesn't exist in the list! ")


# This function is used when the user has confirmed and is ready to commit the changes made in the local list into the text file.
def save_to_file(coll):
    try:
        with open('list.txt', 'w') as file:
            for content in coll:
                file.write(content + '\n')
                print(content)
            print("\nData has been applied to the file!\n")
    except Exception as e:
        print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


# This function will ask the user for an input and then ask to confirm if it is correct, if not the continue statement is used which will replenish the loop and start again.
# If the user wants to exit the function they can enter '//' on user_input, *Note that you can only leave the function on user_input and not confirm_user_input, meaning that you would need to enter N on confirm then type '//'*
def user_function_with_confirm():
    while True:
        try:
            user_input = input("Type '//' to return\n>>> ")  # Before the function is called a print message will complete the beginning of this message.
            if user_input == '//':  # Allows the user to leave the current function
                return False
            confirm_user_input = input(f"Is this correct? -- {user_input} --\n\nY/N: \n>>> ")
            match confirm_user_input.lower():
                case 'y':
                    return user_input
                case 'n':
                    print("Please try again: ")
                    continue
                case _:
                    print("\nInvalid option, please try again:")

        except ValueError as e:
            print(f"ERROR! {e} has caused an Value error!")
        except Exception as e:
            print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


# When called this function will print each line of the list with a number on each item in ascending order, which makes the list easier to read.
def for_print_function(coll):
    val = 0  # This variable is responsible for the item number and will increment once each loop, giving each item an ascending  number.
    print("\n\n-----------------------------\nList's current contents:")
    for content in coll:
        val += 1
        print(f"{val}){content}")
    print("-----------------------------")


# list_sorting function is alot like the for_print_function but will instead sort the list and print a table consisting of unsorted and sorted.
# The function will define an empty list called temporary list and will use a for loop which will append each item from coll then will sort the temporary list meaning
# that the list coll which the whole program uses won't be affected, then a for loop is again used but will print each item of both unsorted and sorted alongside each other
# simultaneously in a table. The table has a feature depending on the size of the item inside both lists will determine how many spaces are added, this ensures the walls
# don't move and stay connected as column.
def list_sorting_table(coll):  # ToDo ~ make the function modular in size, E.g increase amount of '=====' borders depending on the size. !!!!
    temporary_list = []
    for x in coll:
        temporary_list.append(x)
    temporary_list.sort()
    print("\n\n|===================================|\n|     Unsorted     |     Sorted     |")  # 19 | 15
    for content1, content2 in zip(coll, temporary_list):
        print("|", content1, " "*(15-len(content1)), "|", content2, " "*(13-len(content2)), "|")
    print("|===================================|\n\n")


# name_or_index_function is used when a function that uses user input that might need to use a keyword or index, mainly if there are multiple
# items with the same name, indexes are used.
# The function also utilises nested function as the functions within only work in this work flow.
def name_or_index_function(coll):
    try:
        # This function will ask the user for an index of an item and then return the integer
        def index_function():
            for_print_function(coll)
            input_target_index = int(input("Enter the item's index number:\n>>> "))
            return input_target_index

        # This function will ask the user for the name of an item and then will find the item in the list then
        # will get the index position of the item by using its name.
        def name_function():
            for_print_function(coll)
            input_target_name = input("Enter the item's name:\n>>> ")
            for target in range(len(coll)):
                if coll[target] == input_target_name:
                    return target
            return input_target_name

        user_input = input("Type '//' to return to main menu:\nDo you want to use item index or name? \n1)Index\n2)Name\n>>> ")
        if user_input == '//':  # Returns to the main menu
            return False
        if user_input == '1':
            target_input = index_function()
            return target_input
        elif user_input == '2':
            target_input = name_function()
            return target_input
        #  I could use return target_input here but for some reason pycharm gives me a warning doing so.
    except ValueError:
        print("Value Error!")
    except Exception as e:
        print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


if __name__ == '__main__':
    main()
