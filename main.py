from rich.console import Console
from rich.table import Table
import readchar
import os

# Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

console = Console()
todos = {"eat apple": "No", "put banana somewhere": "Yes", "Fuck Orange": "No", "Yeet grape": "Yes"}
my_list_keys = list(todos.keys())

# Initialize the table
table = Table(show_header=True, header_style="bold", title="Todos")
table.add_column("Index")
table.add_column("Todo")
table.add_column("Done?")

# Function to update the table display
# make text strikethrough when value == Yes
def update_table(selected_row):
    new_table = Table(show_header=True, header_style="bold", title="Todos")
    new_table.add_column("Index")
    new_table.add_column("Todo")
    new_table.add_column("Done?")

    for index, key in enumerate(my_list_keys):
        # make text strikethrough when todos at index == Yes
        result = ""
        if todos[key] == "Yes":
            for c in key:
                result += c + "\u0336"

            if index == selected_row:
                new_table.add_row(str(index), result, todos[key], style="bold cyan")
            else:
                new_table.add_row(str(index), result, todos[key])
        else:
            if index == selected_row:
                new_table.add_row(str(index), key, todos[key], style="bold cyan")
            else:
                new_table.add_row(str(index), key, todos[key])

    return new_table

# Function to change the "Done?" status of the selected todo
def change_text(selected_row):
    # Get the key of the selected row
    key = my_list_keys[selected_row]

    # new value equals to the opposite of the current value
    new_value = "Yes" if todos[key] == "No" else "No"

    # Update the todos dictionary with the new value
    todos[key] = new_value

    # Update the table with the new values
    current_table = update_table(selected_row)

    # Print the updated table
    console.clear()
    console.print(current_table)

# Move the current row down
def move_down(current_row):
    if current_row < len(my_list_keys) - 1:
        current_row += 1
    return current_row

# Move the current row up
def move_up(current_row):
    if current_row > 0:
        current_row -= 1
    return current_row

# Function to add a new todo to the table
def add_todo():
    new_todo = input("Enter the new todo: ")
    todos[new_todo] = "No"
    my_list_keys.append(new_todo)  # Add the new todo key to the list of keys

# Function to delete the selected todo from the table
def delete_todo(selected_row):
    # Get the key of the selected row
    todo = my_list_keys[selected_row]

    # Remove the todo from the todos dictionary and list of keys
    del todos[todo]
    my_list_keys.remove(todo)

# Function to save the todos to a file
def save_todos():
    with open("todos.txt", "w") as f:
        for key, value in todos.items():
            f.write(f"{key},{value}\n")

# Function to load the todos from a file
def load_todos():
    global todos, my_list_keys

    # Check if the file exists
    if os.path.exists("todos.txt"):
        # Open the file for reading
        with open("todos.txt", "r") as f:
            # Read the contents of the file
            file_contents = f.read()

            # Split the contents into lines
            lines = file_contents.splitlines()

            # Parse the lines into a dictionary
            todos = {}
            for line in lines:
                key, value = line.split(",")
                todos[key.strip()] = value.strip()

            # Update the list of keys
            my_list_keys = list(todos.keys())
    else:
        # If the file does not exist, use the default todos
        todos = {"eat apple": "No", "put banana somewhere": "Yes", "Fuck Orange": "No", "Yeet grape": "Yes"}
        my_list_keys = list(todos.keys())

# Main function
def main():
    # Load the todos from a file
    load_todos()

    # Set the initial current row to 0
    current_row = 0

    # Print the initial table
    current_table = update_table(current_row)
    console.print(current_table)

    # Enter the main loop
    while True:
        # Get the user input
        key_press = readchar.readkey()

        # Handle the user input
        if key_press == "j":
            current_row = move_down(current_row)
            current_table = update_table(current_row)
            console.clear()
            console.print(current_table)
        elif key_press == "k":
            current_row = move_up(current_row)
            current_table = update_table(current_row)
            console.clear()
            console.print(current_table)
        elif key_press == "c":
            change_text(current_row)
        elif key_press == "a":
            add_todo()
            current_row = len(my_list_keys) - 1
            current_table = update_table(current_row)
            console.clear()
            console.print(current_table)
        elif key_press == "d":
            delete_todo(current_row)
            if current_row > len(my_list_keys) - 1:
                current_row = len(my_list_keys) - 1
            current_table = update_table(current_row)
            console.clear()
            console.print(current_table)
        elif key_press == "s":
            save_todos()
        elif key_press == "q":
            break
#
#        if new_row != selected_row:
#            selected_row = new_row
#            current_table = update_table(selected_row)
#            console.clear()
#            console.print(current_table)

if __name__ == "__main__":
    main()