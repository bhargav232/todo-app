import functions
import PySimpleGUI as sg
import time
sg.theme("Black")
clock = sg.Text("", key="clock")
label = sg.Text('Enter a todo')
Input_box = sg.InputText(tooltip="enter a todo", key='todo')
Add_button = sg.Button(key="ADD", image_source="add.png", tooltip="add todo",mouseover_colors="LightBlue" )
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
Edit_button = sg.Button("EDIT")
Complete_button = sg.Button("Complete")
Exit_button = sg.Button("Exit")
layout = [[clock],[label], [Input_box, Add_button], [list_box, Edit_button, Complete_button], [Exit_button]]
window = sg.Window('My Todo App', layout=layout, font=('Helvetica', 20))

while 1:
    value, item = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d %y, %H:%M:%S"))
    print(value)
    print(item)
    match value:
        case "ADD":
            new_todo = item['todo'] + "\n"
            todos = functions.get_todos()
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "EDIT":
            try:
                new_todo = item['todo']
                todos_to_edit = item['todos'][0]
                todos = functions.get_todos()
                i = todos.index(todos_to_edit)
                todos[i] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("please select an item first!", font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_remove = item['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("please select an item first!", font=('Helvetica', 20))
        case "todos":
            window['todo'].update(value=item['todos'][0])
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break
print("see you next time!")
window.close()

