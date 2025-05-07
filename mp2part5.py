def grade_calculator():
    scores = []
    while True:
        print ("\nMenu: \n1. Add Score\n2. Calculate Average\n3. Exit")
        choice = input ("Enter your choice (1-3): ")

        if choice == '1':
            subject = input("Enter the subject: ")
            try:
                score = float(input("Enter your score: "))
                scores.append(score)
                print ("Score added.")
            except ValueError:
                print ("Invalid score.")
        elif choice == '2':
            if scores:
                average = sum(scores) / len(scores)
                print (f"Average Grade: {average:.2f}")
            else:
                print("No scores to calculate average.")
        elif choice == '3':
            print ("Exiting grade calculator.")
            break
        else:
            print ("Invalid choice. Please enter 1-3.")
grade_calculator()