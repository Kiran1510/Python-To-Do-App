def get_todos(filepath="todos.txt"):
    """
    Read todos from a text file.

    Args:
        filepath (str): Path to the todos file (default: "todos.txt")

    Returns:
        list: List of todo items, each ending with a newline character
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args, filepath="todos.txt"):
    """
    Write todos to a text file, overwriting existing content.

    Args:
        todos_args (list): List of todo items to write
        filepath (str): Path to the todos file (default: "todos.txt")
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_args)