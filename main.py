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


# Main application loop
while True:
    user_action = input("Type add, show, edit, complete or exit:").strip()

    if user_action.startswith("add"):
        # Extract todo text after "add " command and append newline for file formatting
        todo = user_action[4:] + "\n"

        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        # Strip newlines for clean display
        refactored_todos = [item.strip("\n") for item in todos]

        # Display with 1-based indexing
        for index, item in enumerate(refactored_todos):
            print(f"{index + 1}:{item}")

    elif user_action.startswith("edit"):
        try:
            # Convert to 0-based index
            number = int(user_action[5:]) - 1

            todos = get_todos()
            new_todo = input("Enter new todo:")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except (IndexError, ValueError):
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            # Convert to 0-based index
            index = int(user_action[9:]) - 1

            todos = get_todos()
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)

            print(f"Todo '{todo_to_remove}' was removed from the list.")

        except (IndexError, ValueError):
            print("No such item with that number")
            continue

    elif "exit" in user_action:
        break

print("Goodbye!")
