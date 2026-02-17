# runs indefinitely until the user types "exit"
while True:

    # prompt user for an action and strip any whitespaces
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()


    # add new todo
    if "add" in user_action:
        # Get the new todo from user, append newline for file formatting
        todo = user_action[4:]

        # read all existing todos from file
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        todos.append(todo)

        # append the new todo to the list and overwrite the file
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    # show all todos
    elif "show" in user_action:
        # Read all todos from file
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # strip trailing newline characters from each todo for clean display
        refactored_todos = []
        for item in todos:
            new_item = item.strip("\n")
            refactored_todos.append(new_item)

        # display each todo with a 1-based index number
        for index, item in enumerate(refactored_todos):
            print(f"{index + 1}:{item}")

    # edit an existing todo
    elif "edit" in user_action:
        # get which todo to edit
        number = int(user_action[5:])
        number = number - 1

        # open and read the txt file
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # replace the selected todo in the list
        new_todo = input("Enter new todo:")
        todos[number] = new_todo + '\n'

        #write edited todos to the txt file
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    # mark a todo as complete, deleting it
    elif "complete" in user_action :
        # get which todo to remove
        number = int(user_action[9:])

        #open the file
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        #defining internal working index
        index = number - 1

        #getting the todos to be removed
        todo_to_remove = todos[index].strip("\n")

        #remove the completed todo
        todos.pop(index)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        #print out the removed todos
        message = f"Todo '{todo_to_remove}' was removed from the list."
        print(message)

    # exit app
    elif "exit" in user_action:
        break  # breaks out of the while True loop

# goodbye statement
print("Goodbye!")