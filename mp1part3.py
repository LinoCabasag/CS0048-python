'''
Fitness Tracker Program
This program allows users to:
- Add steps to their total step count
- View their total steps
- Calculate calories burned based on steps (0.04 calories per step)
'''

# Initialize total steps
total_steps = 0

# Main program loop
while True:
    # Display menu
    print("\n--- Fitness Tracker ---")
    print("1. Add Steps")
    print("2. View Total Steps")
    print("3. View Calories Burned")
    print("4. Exit")
    
    # Get user choice
    choice = input("Enter choice: ")
    
    # Process the user's choice
    if choice == "1":
        # Add steps
        try:
            steps = int(input("How many steps? "))
            if steps > 0:
                total_steps += steps
                print(f"{steps} steps added!")
            else:
                print("Please enter a positive number of steps.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    elif choice == "2":
        # View total steps
        print(f"Total Steps: {total_steps}")
        
    elif choice == "3":
        # Calculate and view calories burned
        calories = total_steps * 0.04
        print(f"Calories Burned: {calories:.2f} calories")
        
    elif choice == "4":
        # Exit the program
        print("Keep moving! Goodbye!")
        break
        
    else:
        # Handle invalid menu choices
        print("Invalid choice. Please enter a number between 1 and 4.")