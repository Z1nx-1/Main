
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
            user_input = input("----------MAIN MENU----------\n1)Add to list\n2)Search list\n3)Remove from list\n4)Save changes\n5)Cancel changes/Refresh\n6)Print list\n-----------------------------\n")
            if user_input == '1':
                add_to_list(coll)
            elif user_input == '2':
                search_list(coll)
            elif user_input == '3':
                remove_list(coll)
            elif user_input == '4':
                save_to_file(coll)
            elif user_input == '5':
                main()  # by recalling the main() function the list 'coll' will get redefined with 'coll = list_function()' at the start of main().
                for content in coll:
                    print(content)
            elif user_input == '6':
                val = 0
                print("\n\n------")
                for content in coll:  # This for-loop will give each item in the list an ascending number.
                    val += 1
                    print(f"{val}){content}")
                print("------\n\n")
            else:
                print("\nInvalid option, please try again:\n\n\n")
    except ValueError as e:
        print(f"{e} has caused an error")


# This function will ask for user input that will be appended to the end of the 'coll' list.
def add_to_list(coll):
    try:
        user_input = input("\nType '//' to go back\nWhat do you want to add?\n")
        if user_input == '//':
            print("\n")
            return
        confirm = input(f"\nIs this correct? {user_input} \nY/N: ")
        if confirm.lower() == 'y':
            coll.append(user_input)
            print(f"\n\n{coll}\n\n")
        elif confirm.lower() == 'n':
            add_to_list(coll)

        else:
            print("\n\n\nERROR, please enter a valid option: ")
    except ValueError:
        print("ERROR!")


# This function gives the user the ability to search the list for a specific item.
def search_list(coll):
    try:
        target = input("\nType '//' to go back\nEnter name you want to search: ")
        if target == '//':
            print("\n")
            return
        if target in coll:
            print(f"{target} has been found in the file!")
        else:
            print("That is not in the file! ")
    except ValueError:
        print("ERROR!")


# This function, like the 'search_list' function will ask the user for an item name and then remove that item from the list.
def remove_list(coll):
    try:
        for content in coll:
            print(content)
        target = input("\nType '//' to go back\nWhich item would you like to remove?\n")
        if target == '//':
            print(f"\n")
            return
        coll.remove(target)
        print("\n\n\nUpdated list: ")
        for content in coll:
            print(content)
    except ValueError:
        print("ERROR! That item doesn't exist in the list! ")


# This function is used when the user has confirmed and is ready to commit the changes made in the local list into the text file.
def save_to_file(coll):
    with open('list.txt', 'w') as file:
        for content in coll:
            file.write(content + '\n')
            print(content)


if __name__ == '__main__':
    main()
