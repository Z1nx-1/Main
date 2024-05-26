
# This function will be called then assign the contents of the text file 'list.txt' to a list called 'coll'(Collection).
def list_function():
    global coll
    with open('list.txt', 'r') as file:
        coll = file.read().split()


# This function acts as a main menu that will give the user access to each parts of the program in an easy manner.
def main():
    try:
        while True:
            user_input = input("----------MAIN MENU----------\n1)Add to list\n2)Search list\n3)Remove from list\n4)Save changes\n5)Cancel changes/Refresh\n6)Print list\n-----------------------------\n")
            if user_input == '1':
                add_to_list()
            elif user_input == '2':
                search_list()
            elif user_input == '3':
                remove_list()
            elif user_input == '4':
                save_to_file()
            elif user_input == '5':
                list_function()
                print(coll)
            elif user_input == '6':
                # This for-loop will give each item in the list an ascending number.
                val = 0
                print("\n\n------")
                for content in coll:
                    val += 1
                    print(f"{val}){content}")
                print("------\n\n")
            else:
                print("\nInvalid option, please try again:\n\n\n")
    except ValueError as e:
        print(f"{e} has caused an error")


# This function will ask for user input that will be appended to the end of the 'coll' list.
def add_to_list():
    while True:
        try:
            user_input = input("\nType '//' to go back\nWhat do you want to add? ")
            if user_input == '//':
                break
            confirm = input(f"Is this correct? {user_input} \nY/N: ")
            if confirm.lower() == 'y':
                coll.append(user_input)
                print(coll)

            elif confirm.lower() == 'n':
                continue

            else:
                print("\n\n\nERROR, please enter a valid option: ")
        except ValueError:
            print("ERROR!")


# This function is used when the user has confirmed and is ready to commit the changes made in the local list into the text file.
def save_to_file():
    with open('list.txt', 'w') as file:
        for content in coll:
            file.write(content + '\n')
            print(content)


# This function gives the user the ability to search the list for a specific item.
def search_list():
    while True:
        try:
            target = input("\nType '//' to go back\nEnter name you want to search: ")
            if target == '//':
                break
            if target.lower() in coll:
                print(f"{target} has been found in the file!")
            else:
                print("That is not in the file! ")
        except ValueError:
            print("ERROR!")


# This function, like the 'search_list' function will ask the user for an item name and then remove that item from the list.
def remove_list():
    while True:
        try:
            target = input("\nType '//' to go back\nEnter the name you want to remove: ")
            if target == '//':
                break
            coll.remove(target)
            for content in coll:
                print(content)
            print(coll)
        except ValueError:
            print("ERROR!")


if __name__ == '__main__':
    coll = []
    list_function()
    main()
