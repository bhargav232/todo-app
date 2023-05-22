from zip_com_bonus8 import make_archive
import PySimpleGUI as sg

l1 = sg.Text("select files to compress: ")
b1 = sg.InputText(tooltip="enter a files to compress")
button1 = sg.FilesBrowse("Choose", key='files')
l2 = sg.Text("select destination folder: ")
b2 = sg.InputText(tooltip="enter a destination folder")
button2 = sg.FolderBrowse("Choose", key='folder')
button3 = sg.Button("compress")
output = sg.Text(key='output',text_color='blue')
window = sg.Window("file zipper", [[l1, b1, button1], [l2, b2, button2], [button3, output]])
while 1:
    value, item = window.read()
    match value:
        case 'compress':
            file_paths = item['files'].split(";")
            folder_path = item['folder']
            make_archive(file_paths, folder_path)
            window['output'].update(value='compression completed!')
        case sg.WINDOW_CLOSED:
            break
print("bye, see you soon!")
window.close()
