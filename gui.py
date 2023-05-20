import functions
import PySimpleGUI as sg

label = sg.Text('Enter a todo')
Input_box = sg.InputText(tooltip="enter a todo", key='todo')
button = sg.Button("ADD")
window = sg.Window('My Todo App', layout=[[label], [Input_box, button]])
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
        case sg.WINDOW_CLOSED:
            break
window.close()

