# Adds a task to the list
def add_task(tasks):
    try:
        title = input("Enter the task: ")
        if title:
            tasks[title] = {}  # Initialize the task with an empty list for details
            print(f"Task '{title}' added successfully!\n")
        else:
            raise ValueError("Task title cannot be empty")
    except ValueError as e:
        print(f"Error: {e}\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")
    else:
        print("Task added without any issues.\n")
    
# Remove a task from the list
def remove_task(tasks):
    try:
        title = input("Enter the task you want to remove: ")
        if title in tasks:
            del tasks[title]
            print(f"Task '{title}' removed successfully!\n")
        else:
            raise KeyError("Task not found")
    except KeyError as e:
        print(f"Error: {e}\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")
    else:
        print("Task removed succesfully.\n")

# View the list of tasks
def display_tasks(tasks):
    try:
        if tasks:
            print("Here is your list of tasks:\n")
            for title, details in tasks.items():
                print(f"Task: {title}")
        else:
            raise ValueError("No tasks found")
    except ValueError as e:
        print(f"Error: {e}\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")
    else:
        print("Tasks displayed.\n")
    

# Main function for user interactions
def main():
    tasks = {}
    while True:
        print("Welcome to your task list!")
        print("\nChoose an option:")
        print("\n1. Add a task")
        print("\n2. Remove a task")
        print("\n3. View tasks list")
        print("\n4. Quit")
        choice = input("\nEnter your choice (1/2/3/4): ")

        try:
            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                remove_task(tasks)
            elif choice == '3':
                display_tasks(tasks)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                raise ValueError("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")
        finally:
            print("Do you want to do anything else?.\n")

# Start the program
if __name__ == "__main__":
    main()
