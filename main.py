
# This function will be called then assign the contents of the text file 'list.txt' to a list called 'coll'(Collection).
def list_function():
    with open('list.txt', 'r') as file:
        coll = file.read().split()
        return coll


# This function acts as a main menu that will give the user access to each parts of the program in an easy manner.
def main():
    while True:
        try:
            coll = list_function()
            user_input = int(input("----------MAIN MENU----------\n1)Add to list\n2)Search list\n3)Remove from list\n4)Save changes\n5)Cancel changes/Refresh\n6)Print list\n-----------------------------\n"))
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
                    main()  # by recalling the main() function the list 'coll' will get redefined with 'coll = list_function()' at the start of main().
                case 6:
                    for_print_function(coll)
                    print("------\n\n")
                case _:
                    print("\nInvalid option, please try again:")
        except ValueError as e:
            print(f"ERROR! {e} has caused an Value error!")
        except Exception as e:
            print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


def lower_case_coll_function(coll):
    exported_data = [x.lower() for x in coll]
    temporary_coll = exported_data
    return temporary_coll


def user_function():
    while True:
        try:
            user_input = input("Enter something: ")
            if user_input == '//':  # concept ~ The user can enter two forward slashes to leave exit out of a function.
                pass  # Implement a way for the user to leave the current function that they may have accidentally been called.
            confirm_user_input = input(f"Is this correct? -- {user_input} --\n")
            match confirm_user_input.lower():
                case 'y':
                    return user_input
                case 'n':
                    continue
                case _:
                    print("\nInvalid option, please try again:")
        except ValueError as e:
            print(f"ERROR! {e} has caused an Value error!")
        except Exception as e:
            print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


# This function will ask for user input that will be appended to the end of the 'coll' list.
def add_to_list(coll):
    try:
        for_print_function(coll)
        user_input = user_function()
        coll.append(user_input)
    except Exception as e:
        print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


# This function gives the user the ability to search the list for a specific item.
# (P1) The exported_data variable is defined by the main coll list with the addition of a for loop with will set each item in the list to lower case.
# (P2) Then the items/data inside exported_data will be defined within temporary_coll.
# (P3) The reason for converting to lower case, so the user has an easier time searching for items, otherwise you would need to have exact capitalization.
def search_list(coll):
    while True:
        try:
            for_print_function(coll)
            temporary_coll = lower_case_coll_function(coll)
            target = user_function()
            if target.lower() in temporary_coll:
                print(f"{target} has been found in the file!")
            else:
                print(f"{target} has not been found in the file!")
        except ValueError:
            print("ERROR!")
        except Exception as e:
            print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


# This function, like the 'search_list' function will ask the user for an item name and then remove that item from the list.
def remove_list(coll):
    val = 0
    while True:
        try:
            if val == 0:  # The val variable is used to stop the initial unedited version of the list appearing after a removal of an item, this works due to the first loop doesn't increment val which means it can print the initial list.
                for_print_function(coll)
            target = user_function()
            coll.remove(target)
            print("\n\n\nUpdated list: ")
            for_print_function(coll)
            val += 1
        except ValueError:
            print("ERROR! That item doesn't exist in the list! ")


# This function is used when the user has confirmed and is ready to commit the changes made in the local list into the text file.
def save_to_file(coll):
    try:
        with open('list.txt', 'w') as file:
            for content in coll:
                file.write(content + '\n')
                print(content)
    except Exception as e:
        print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


# When called this function will print each line of the list with a number on each item in ascending order, which makes the list easier to read.
def for_print_function(coll):
    val = 0  # This variable is responsible for the item number and will increment once each loop, giving each item a number.
    print("\n\n------\nList's current contents:")
    for content in coll:
        val += 1
        print(f"{val}){content}")


if __name__ == '__main__':
    main()


"""
# This function will ask the user for an input, which is used in add_to_list, search_list, remove list.
# The main purpose of this function is to shorten code as the user_input variable is used many times in each input functions.
def user_input_function():
    while True:
        try:
            user_input = input("Enter something: ")
            if user_input == '//':
                return False
            return user_input
        except ValueError as e:
            print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")




# This functions purpose is to confirm user actions before applying changes.
def user_confirm_action(user_input):
   while True:
        try:
            confirm_user_action = input(f"Is this correct? -- {user_input} --\n")
            match confirm_user_action.lower():
                case '//':
                    return False
                case 'y':
                    break  # Breaks from this functions loop and continues the loop that called this function which will execute the code that is confirmed by the user.
                case 'n':
                    user_input_function()
                case _:
                    print("\nInvalid option, please try again:")
        except ValueError:
            print("ERROR! ")




def ignore(user_input, coll):
    match user_confirm_action(user_input):
        case True:
            coll.append(user_input)
            print(f"\n\n{coll}\n\n")
        case False:
            pass

"""