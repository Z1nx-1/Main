
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
            user_input = int(input("----------MAIN MENU----------\n1)Add to list\n2)Search list\n3)Remove from list\n4)Save changes\n5)Cancel changes/Refresh\n6)Print list\n7)Sort table\n-----------------------------\n>>> "))
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
                    list_sorting(coll)
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
            coll.append(user_input)  # The data that the user wants to add into the list will be added into the end.
        except Exception as e:
            print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


# This function gives the user the ability to search the list for a specific item.
# (P1) The lower_case_coll_function will convert all items in the coll list into lower case.
# (P2) The purpose for this is to allow the user to enter an item name without worrying about capitalization.
def search_list(coll):
    while True:
        try:
            for_print_function(coll)
            print("Enter the name of the item you would like to search: ")
            lower_case_converted_list = lower_case_coll_function(coll)
            target = user_function()
            if target is False:
                break
            match target.lower() in lower_case_converted_list:
                case True:
                    print(f"{target} has been found in the file!")
                case False:
                    print(f"{target} has not been found in the file!")
                case _:
                    print("ERROR")
        except ValueError:
            print("ERROR!")
        except Exception as e:
            print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


# This function, like the 'search_list' function will ask the user for an item name and then remove that item from the list.
# Implement a way for the user to remove an item with the index number of the item.
def remove_list(coll):
    while True:
        try:
            for_print_function(coll)
            target = user_function_with_confirm()
            if target is False:
                break
            elif target in coll:
                print(f"{target} found and has been removed!\n")
                coll.remove(target)
            else:
                print(f"{target} has not been found, no changes have been made!")
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
            user_input = input("Type '//' to return\n>>> ")
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


# This function is almost identical to user_function_with_confirm but without the 'confirm' variable.
def user_function():
    while True:
        try:
            user_input = input("\nType '//' to return to main menu:\n>>> ")
            if user_input == '//':  # concept ~ The user can enter two forward slashes to leave exit out of a function.
                return False
            return user_input
        except ValueError as e:
            print(f"ERROR! {e} has caused an Value error!")
        except Exception as e:
            print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


# When called this function will print each line of the list with a number on each item in ascending order, which makes the list easier to read.
def for_print_function(coll):
    val = 0  # This variable is responsible for the item number and will increment once each loop, giving each item a number.
    print("\n\n-----------------------------\nList's current contents:")
    for content in coll:
        val += 1
        print(f"{val}){content}")
    print("-----------------------------")


# The use of this function is for the ease of use for the user, otherwise the user would have to worry about capitalization.
# The exported_data is a list which will read all the contents of the list 'coll' with a for loop which will convert each item into lower case -
# thus defining exported data with all lower case item names.
def lower_case_coll_function(coll):
    exported_data = [x.lower() for x in coll]
    return exported_data


# list_sorting function is alot like the for_print_function but will instead sort the list and print a table consisting of unsorted and sorted.
# The function will define an empty list called temporary list and will use a for loop which will append each item from coll then will sort the temporary list meaning
# that the list coll which the whole program uses won't be affected, then a for loop is again used but will print each item of both unsorted and sorted alongside each other
# simultaneously in a table. The table has a feature depending on the size of the item inside both lists will determine how many spaces are added, this ensures the walls
# don't move and stay connected as column.
def list_sorting(coll):  # ToDo ~ make the function modular in size, i.e increase amount of '=====' borders depending on the size.
    temporary_list = []
    for x in coll:
        temporary_list.append(x)
    temporary_list.sort()
    print("\n\n|===================================|\n|     Unsorted     |     Sorted     |")  # 19 | 15
    for content1, content2 in zip(coll, temporary_list):
        print("|", content1, " "*(15-len(content1)), "|", content2, " "*(13-len(content2)), "|")
    print("|===================================|\n\n")


if __name__ == '__main__':
    main()
