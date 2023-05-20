import functions
import PySimpleGUI as sg

label = sg.Text('Enter a todo')
Input_box = sg.InputText(tooltip="enter a todo", key='todo')
button1 = sg.Button("ADD")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
button2 = sg.Button("EDIT")
window = sg.Window('My Todo App', layout=[[label], [Input_box, button1],
                                          [list_box, button2]])
while 1:
    value, item = window.read()
    print(value)
    print(item)
    match value:
        case "ADD":
            new_todo = item['todo'] + "\n"
            todos = functions.get_todos()
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "EDIT":
            new_todo = item['todo']
            todos_to_edit = item['todos'][0]
            todos = functions.get_todos()
            i = todos.index(todos_to_edit)
            todos[i] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=item['todos'][0])
        case sg.WINDOW_CLOSED:
            break
window.close()

