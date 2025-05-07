def todo_list():
    tasks = []
    while True:
        print ("\nMenu: \n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input ("Enter the task to add: ")
            tasks.append(task)
            print("Task added.")
        elif choice == '2':
            task = input ("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print ("Task removed.")
            else:
                print ("Task not found.")
        elif choice =='3':
            if not tasks:
                print ("No tasks in the list.")
            else:
                print ("Tasks:")
                for t in tasks:
                    print (f"- {t}")
        elif choice == '4':
            break
        else: 
            print ("Invalid choice. Please enter 1-4.")

todo_list()