
list = []


def main():
    try:
        while True:
            user_input = input("1) Add to list\n2) search list\n")
            if user_input == '1':
                add_to_list()
            elif user_input == '2':
                search_list()
    except ValueError as e:
        print(f"{e} has caused an error")


def add_to_list():
    while True:
        user_input = '\n' + input("What do you want to add? ")
        confirm = input(f"Is this correct? {user_input} \nY/N: ")
        if confirm == 'y':
            list.append(user_input)
            save_to_file()

        elif confirm == 'n':
            print("Please start again. ")
            continue

        else:
            print("\n\n\nERROR, please enter a valid option: ")


def save_to_file():
    with open('list.txt', 'w') as file:
        for content in list:
            file.write(content)
            print(content)


def list_function():
    with open('list.txt', 'r') as file:
        list.append(file.read().split('\n'))
        print(list)


def search_list():
    pass

if __name__ == '__main__':
    list_function()
    main()
