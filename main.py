from rich.console import Console
from rich.table import Table
import readchar

console = Console()
todos = {"eat apple": "False", "put banana somewhere": "True", "Fuck Orange": "False", "Yeet grape": "True"}
my_list_keys = list(todos.keys())

table = Table(show_header=True, header_style="bold", title="Todos")
table.add_column("Index")
table.add_column("Todo")
table.add_column("Done?")

# Add table rows
for index, key in enumerate(my_list_keys):
    table.add_row(str(index), key, todos[key])

console.print(table)

# Store the currently selected row index
selected_row = 0

# Function to update the table display
def update_table():
    # Clear the console
    console.clear()

    # Create a new table with updated selection
    new_table = Table(show_header=True, header_style="bold", title="Todos")
    new_table.add_column("Index")
    new_table.add_column("Todo")
    new_table.add_column("Done?")

    for index, key in enumerate(my_list_keys):
        if index == selected_row:
            new_table.add_row(str(index), key, todos[key], style="bold cyan")
        else:
            new_table.add_row(str(index), key, todos[key])

    console.print(new_table)

# Function to change the "Done?" status of the selected todo
def change_text():
    todo = my_list_keys[selected_row]
    current_status = todos[todo]
    if current_status == "False":
        todos[todo] = "True"
    elif current_status == "True":
        todos[todo] = "False"
    update_table()

# Function to add a new todo to the table
def add_todo():
    new_todo = input("Enter the new todo: ")
    todos[new_todo] = "False"
    my_list_keys.append(new_todo)  # Add the new todo key to the list of keys
    update_table()

# Function to delete the selected todo from the table
def delete_todo():
    todo = my_list_keys[selected_row]
    del todos[todo]
    my_list_keys.remove(todo)  # Remove the todo key from the list of keys
    update_table()

# Main loop to handle navigation and other actions
while True:
    key = readchar.readkey()

    if key == "j":
        selected_row = min(selected_row + 1, len(my_list_keys) - 1)
        update_table()
    elif key == "k":
        selected_row = max(selected_row - 1, 0)
        update_table()
    elif key == "c":
        change_text()
    elif key == "a":
        add_todo()
    elif key == "d":
        delete_todo()
    elif key == "q":
        break
