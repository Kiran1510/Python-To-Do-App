# Todo App

A command-line todo list manager built with Python. Add, view, edit, and complete tasks — all stored persistently in a local text file.

## Features

- **Add** todos directly from the command line
- **View** all todos with numbered indices
- **Edit** existing todos by number
- **Complete** (delete) todos with a confirmation message
- **Persistent storage** — todos are saved to `todos.txt` and survive between sessions
- **Error handling** — gracefully handles invalid inputs, missing numbers, and out-of-range indices

## Usage

Run the app:

```
python main.py
```

The app will prompt you to enter a command. Commands are entered in the format `command` or `command value`:

| Command | Example | Description |
|---------|---------|-------------|
| `add` | `add Buy groceries` | Adds a new todo to the list |
| `show` | `show` | Displays all todos with numbered indices |
| `edit` | `edit 2` | Prompts you to replace the todo at position 2 |
| `complete` | `complete 3` | Removes the todo at position 3 and prints a confirmation |
| `exit` | `exit` | Quits the app |

### Example Session

```
Type add, show, edit, complete or exit: add Buy groceries
Type add, show, edit, complete or exit: add Walk the dog
Type add, show, edit, complete or exit: show
1: Buy groceries
2: Walk the dog
Type add, show, edit, complete or exit: complete 1
Todo 'Buy groceries' was removed from the list.
Type add, show, edit, complete or exit: exit
Goodbye!
```

## How It Works

- The app runs in a continuous `while True` loop, prompting the user for input each iteration
- User input is parsed using `startswith()` to determine the command and extract any arguments (e.g., the todo text or item number)
- Todos are stored in `todos.txt`, with each todo on its own line
- A helper function `get_todos()` reads from the file and returns a list of todo strings
- On every add, edit, or complete action, the full list is read from the file, modified in memory, and written back
- Invalid inputs and out-of-range indices are caught using `try/except` blocks for `ValueError` and `IndexError`

## Project Structure

```
todo-app/
├── main.py        # Main application code
└── todos.txt      # Persistent storage for todos
```

## Requirements

- Python 3.10+
- A `todos.txt` file in the same directory (create an empty one if it doesn't exist)
