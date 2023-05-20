import functions
import PySimpleGUI as sg

label = sg.Text('Enter a todo')
Input_box = sg.InputText(tooltip="enter a todo")
button = sg.Button("ADD")
window = sg.Window('My Todo App', layout=[[label], [Input_box, button]])
window.read()
window.close()

