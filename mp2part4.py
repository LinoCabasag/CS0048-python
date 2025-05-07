import random

def number_guessing_game():
    while True:
        print ("\nMenu: \n1. Play Number Guessing Game\n2. Exit")
        choice = input ("Enter your choice (1-2): ")

        if choice == '2':
            print ("Exiting game.")
            break
        elif choice == '1':
            number = random.randint(1, 100)
            attempts = 0
            while True:
                try:
                    guess = int (input("Guess the number (1-100): "))
                except ValueError:
                    print ("Please enter a valid number.")
                    continue

                attempts += 1
                if guess < number:
                    print ("Too low!")
                elif guess >number:
                    print ("Too high!")
                else: 
                    print (f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
            else:
                print ("Invalid choice")
number_guessing_game()