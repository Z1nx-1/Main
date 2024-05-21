
def list_function():
    global coll
    with open('list.txt', 'r') as file:
        coll = file.read().split('\n')


def main():
    try:
        while True:
            user_input = input("1)Add to list\n2)Search list\n3)Remove from list\n4)Save data to file\n5)Print list\n")
            if user_input == '1':
                add_to_list()
            elif user_input == '2':
                search_list()
            elif user_input == '3':
                remove_list()
            elif user_input == '4':
                save_to_file()
            elif user_input == '5':
                val = 0
                print("\n\n------")
                for content in coll:
                    val += 1
                    print(f"{val}) {content}")
                print("------\n\n")
    except ValueError as e:
        print(f"{e} has caused an error")


def add_to_list():
    user_input = '\n' + input("What do you want to add? ")
    confirm = input(f"Is this correct? {user_input} \nY/N: ")
    if confirm == 'y':
        coll.append(user_input)
        save_to_file()

    elif confirm == 'n':
        print("Please start again. ")

    else:
        print("\n\n\nERROR, please enter a valid option: ")


def save_to_file():
    with open('list.txt', 'w') as file:
        for content in coll:
            file.write('\n')
            file.write(content)
            print(content)


def search_list():
    target = input("Enter name you want to search: ")
    if target in coll:
        print("That is in the file! ")

    else:
        print("That is not in the file! ")


def remove_list():
    target = input("Enter the name you want to remove: ")
    coll.remove(target)
    for content in coll:
        print(content)
    print(coll)


if __name__ == '__main__':
    list_function()
    main()
