def get_todos(file_path):
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(file_path, todo_arg):
    with open(file_path, 'w') as file:
        file.writelines(todo_arg)