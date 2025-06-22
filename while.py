tasks = []

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        print("\nYour Tasks:")
        for t in tasks:
            print("- " + t)
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
