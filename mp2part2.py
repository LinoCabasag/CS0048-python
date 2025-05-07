def temperature_converter():
    while True:
        print ("\nMenu: \n1. Convert Celsius to Fahrenheit\n2. Convert Fahrenheit to Celcius\n3. Exit.")
        choice = input ("Enter your choice (1-3): ")

        if choice == '3':
            print ("Exiting Converter...")
            break

        try:
            temp = float(input("Enter temperature: "))
        except ValueError:
            print ("Invalid temperature input.")
            continue
            
        if choice == '1':
            result = ( temp * 9/5) + 32
            print (f"Temperature in Fahrenheit : {result}")
        elif choice == '2':
            result = (temp - 32) * 5/9
            print (f"Temperature in Celsius: {result}")
        else:
            print ("Invalid choice. Please select from 1-3.")

temperature_converter()