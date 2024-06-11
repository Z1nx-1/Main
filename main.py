
# This function will be called then assign the contents of the text file 'list.txt' to a list called 'coll'(Collection).
def list_function():
    with open('list.txt', 'r') as file:
        coll = file.read().split()
        return coll


# This function acts as a main menu that will give the user access to each parts of the program in an easy manner.
def main():
    try:
        coll = list_function()
        while True:
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
                    print("\nInvalid option, please try again:\n\n\n")

    except ValueError as e:
        print(f"ERROR! {e} has caused an Value error!")
    except Exception as e:
        print(f"ERROR!\nA general error has occurred!\nMore info: \n{e}")


# This function will ask for user input that will be appended to the end of the 'coll' list.
def add_to_list(coll):
    while True:
        try:
            for_print_function(coll)
            user_input = input("\nType '//' to go back\nWhat do you want to add?\n")
            if user_input == '//':
                print("\n")
                return

            match user_confirm_action(user_input):
                case True:
                    coll.append(user_input)
                    print(f"\n\n{coll}\n\n")
                case False:
                    continue

            # else:
            #    print("\n\n\nERROR, please enter a valid option: ")
        except ValueError:
            print("ERROR!")


# This function gives the user the ability to search the list for a specific item.
# (P1) The exported_data variable is defined by the main coll list with the addition of a for loop with will set each item in the list to lower case.
# (P2) Then the items/data inside exported_data will be defined within temporary_coll.
# (P3) The reason for converting to lower case, so the user has an easier time searching for items, otherwise you would need to have exact capitalization.
def search_list(coll):
    while True:
        try:
            exported_data = [x.lower() for x in coll]
            temporary_coll = exported_data
            target = input("\nType '//' to go back\nEnter name you want to search: ")
            if target == '//':
                print("\n")
                return
            if target.lower() in temporary_coll:
                print(f"{target} has been found in the file!")
            else:
                print(f"{target} has not been found in the file!")
        except ValueError:
            print("ERROR!")


# This function, like the 'search_list' function will ask the user for an item name and then remove that item from the list.
def remove_list(coll):
    val = 0
    while True:
        try:
            if val == 0:  # The val variable is used to stop the initial unedited version of the list appearing after a removal of an item, this works due to the first loop doesn't increment val which means it can print the initial list.
                for_print_function(coll)
            target = input("\nType '//' to go back\nWhich item would you like to remove?\n")
            if target == '//':
                print(f"\n")
                return
            match user_confirm_action(target):
                case True:
                    coll.remove(target)
                case False:
                    print("Item was not removed: ")
                    continue

            print("\n\n\nUpdated list: ")
            for_print_function(coll)
            val += 1
        except ValueError:
            print("ERROR! That item doesn't exist in the list! ")


# This function is used when the user has confirmed and is ready to commit the changes made in the local list into the text file.
def save_to_file(coll):
    with open('list.txt', 'w') as file:
        for content in coll:
            file.write(content + '\n')
            print(content)


# When called this function will print each line of the list with a number on each item in ascending order, which makes the list easier to read.
def for_print_function(coll):
    val = 0  # This variable is responsible for the item number and will increment once each loop, giving each item a number.
    print("\n\n------\nList's current contents:")
    for content in coll:
        val += 1
        print(f"{val}){content}")


# Function concept: Before applying an action, this function will be called which will be given a parameter which will the users action/input, then will determine if the action proceeds or not.
def user_confirm_action(user_input):
    while True:
        try:
            confirm = input(f"Is this correct? -- {user_input} --\n")
            match confirm.lower():
                case 'y':
                    return True
                case 'n':
                    return False
                case _:
                    print("\nInvalid option, please try again:\n\n\n")
        except ValueError:
            print("ERROR! ")


if __name__ == '__main__':
    main()
