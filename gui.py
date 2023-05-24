import functions
import PySimpleGUI as sg

label = sg.Text('Enter a todo')
Input_box = sg.InputText(tooltip="enter a todo", key='todo')
Add_button = sg.Button("ADD")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
Edit_button = sg.Button("EDIT")
Complete_button = sg.Button("Complete")
Exit_button = sg.Button("Exit")
layout = [[label], [Input_box, Add_button], [list_box, Edit_button, Complete_button], [Exit_button]]
window = sg.Window('My Todo App', layout=layout)
while 1:
    value, item = window.read()
    print(value)
    print(item)
    match value:
        case "ADD":
            todos = functions.get_todos()
            new_todo = item['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "EDIT":
            new_todo = item['todo']
            todos_to_edit = item['todos'][0]
            todos = functions.get_todos()
            i = todos.index(todos_to_edit)
            todos[i] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_remove = item['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_remove)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "todos":
            window['todo'].update(value=item['todos'][0])
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break
print("see you next time!")
window.close()

