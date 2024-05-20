
list = []



def add_to_list():
        user_input = input("What do you want to add? ")
        list.append(user_input)
        print(list)
        return user_input

def save_to_file(user_input):
    with open('list.txt', 'a') as file:
        confirm = input(f"Are you sure you want to add, {user_input}? Y/N: ")
        if confirm == 'y':
            file.write("\n")
            file.write(user_input)
        elif confirm == 'n':
            print("Passing")
            pass


def list_function():
    with open('list.txt', 'r') as file:
        list.append(file.read())


if __name__ == '__main__':
    list_function()
    user_input = add_to_list()
    save_to_file(user_input)