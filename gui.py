from functions import *
import PySimpleGUI as ps
import time

label = ps.Text("What would you like to do: ")
clock = ps.Text(' ', key='clock')

input_box = ps.InputText(tooltip="Enter todo", key="todo")
addB = ps.Button("Add")
list_box = ps.Listbox(values=get_todos("todos.txt"), key='todos', enable_events=True, size=(45, 10))
editB = ps.Button('Edit')
completeB = ps.Button('Complete')
exitB = ps.Button("Exit")

window = ps.Window('My To-Do App',
                   layout=[ [clock],
                            [label],
                            [input_box, addB],
                            [list_box, editB, completeB],
                            [exitB]],

                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = get_todos("todos.txt")
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos("todos.txt", todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edit":
            try:
                todo_edit = values['todos'][0]
                new_todo = values['todo']

                todos = get_todos("todos.txt")
                index = todos.index(todo_edit)
                todos[index] = new_todo
                write_todos("todos.txt", todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                ps.popup("select an item first", font=('Helvetica', 20))
        case 'Complete':
            try:
                todo_complete = values['todos'][0]
                todos = get_todos("todos.txt")
                todos.remove(todo_complete)
                write_todos("todos.txt", todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                ps.popup("select an item first", font=('Helvetica', 20))

        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case ps.WINDOW_CLOSED:
            break

window.close()
