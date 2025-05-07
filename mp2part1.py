def calculator():
    while True:
        print("\nMenu: \n1. Add\n2. Substract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input ("Enter your choice (1-5):")

        if choice == '5':
            print ("Exiting Calculator...")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float (input("Enter First number: "))
                num2 = float (input("Enter second number: "))
            except ValueError:
                print ("Invalid input. Please enter numbers.")
                continue

        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice =='2':
            print (f"Result: {num1 - num2}")
        elif choice == '3':
            print (f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print ("Cannot be divided by zero.")
            else:
                print (f"Result: {num1 / num2}")
    else: 
        print ("Invalid choice. Please enter a number from 1 to")

calculator()