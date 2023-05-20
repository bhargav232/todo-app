from functions import get_todos, write_todos
import time
print("below is a usage of time module")
now = time.strftime("%b %d %y, %H:%M:%S")
print(f"It's now {now}")
while True:
    user_action = (input('what you want to to add, show, edit, complete, and exit? : '))
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        for i, v in enumerate(todos):
            v = v.strip('\n')
            row = f"{i + 1}->{v}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            val = int(user_action[5:])
            # val = int(input("On which index you want edit?: "))
            val = val - 1
            todos = get_todos()
            z = input("Enter new item: ")
            todos[val] = z + '\n'
            write_todos(todos)
        except ValueError:
            print('Not a valid command!')

    elif user_action.startswith('complete'):
        try:
            p = int(user_action[9:])
            p = p - 1
            todos = get_todos()
            todo_to_remove = todos[p].strip('\n')
            todos.pop(p)
            write_todos(todos)
            print(f'The todo->{todo_to_remove} was removed successfully')
        except IndexError:
            print('Value entered is out of range!')
        except ValueError:
            print('Not a valid command!')
    elif user_action.startswith('exit'):
        break

    else:
        print('Please, enter a valid command!')

print('Bye, See you soon!')
