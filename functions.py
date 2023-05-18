FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    """
    Read a text file and return a list of to-do items
    """
    with open(file_path, 'r') as file:
        todos1 = file.readlines()
        return todos1

# print(help(get_todos))


def write_todos(todos_arg, file_path=FILEPATH):
    """
    Write the to-do item list in the text file
    """
    with open(file_path, 'w') as file:
        file.writelines(todos_arg)

        
if __name__== '__main__':
    print(get_todos())
