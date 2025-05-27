FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """Read a text file and return a list
    of todo items
    """
    with open(filepath, "r") as file:
        content = file.readlines()
    return content

def write_todos(todos_arg, filepath = FILEPATH):
    """Write the todo items list in the file"""
    with open(filepath, "w") as f:
        f.writelines(todos_arg)

if __name__ == "__main__":
    print(get_todos())