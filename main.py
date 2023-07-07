from rich.console import Console
from rich.table import Table
import readchar

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
    todo = my_list_keys[selected_row]
    current_status = todos[todo]
    if current_status == "No":
        todos[todo] = "Yes"
    elif current_status == "Yes":
        todos[todo] = "No"

# Function to add a new todo to the table
def add_todo():
    new_todo = input("Enter the new todo: ")
    todos[new_todo] = "No"
    my_list_keys.append(new_todo)  # Add the new todo key to the list of keys

# Function to delete the selected todo from the table
def delete_todo():
    todo = my_list_keys[selected_row]
    del todos[todo]
    my_list_keys.remove(todo)  # Remove the todo key from the list of keys

# Function to save the todos to a file
def save_todos():
    with open("todos.txt", "w") as f:
        for key, value in todos.items():
            f.write(f"{key},{value}\n")

# Function to load the todos from a file
def load_todos():
    try:
        with open("todos.txt", "r") as f:
            for line in f:
                key, value = line.strip().split(",")
                todos[key] = value
                my_list_keys.append(key)
    except FileNotFoundError:
        print("No todos.txt file found. Starting with no todos.")

# Main function
def main():
    # Load the todos from a file
    load_todos()

    # Print the initial table
    selected_row = 0
    current_table = update_table(selected_row)
    console.print(current_table)

    # Main loop to handle navigation and other actions
    while True:
        key = readchar.readkey()

        if key == "j":
            selected_row = min(selected_row + 1, len(my_list_keys) - 1)
        elif key == "k":
            selected_row = max(selected_row - 1, 0)
        elif key == "c":
            change_text(selected_row)
        elif key == "a":
            add_todo()
        elif key == "d":
            delete_todo()
        elif key == "s":
            save_todos()
        elif key == "q":
            break

        current_table = update_table(selected_row)
        console.print(current_table)

if __name__ == "__main__":
    main()
