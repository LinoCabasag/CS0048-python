'''
Grocery Store Management Program
This program allows users to:
- View available items
- Add items to cart
- Calculate total cost with VAT
'''

item_list = [
    ('Rice', 50),
    ('Eggs', 7),
    ('Milk', 60),
    ('Bread', 35)
]

items = dict(item_list)

cart = {}

while True:
    print('\n--- Grocery Store --- ')
    print('1. View Items')
    print('2. Add to Cart')
    print('3. Checkout')
    print('4. Exit')

    choice = input('Enter choice: ')
    
    if choice == "1":
        print('\n--- Available Items ---')
        for index, (item, price) in enumerate(item_list, 1):
            print(f"{index}. {item}: ₱{price}")
            
    elif choice == "2":
        print('\n--- Available Items ---')
        for index, (item, price) in enumerate(item_list, 1):
            print(f"{index}. {item}: ₱{price}")
            
        try:
            item_number = int(input('\nEnter item number: '))
            
            if 1 <= item_number <= len(item_list):
                item_name = item_list[item_number-1][0]
                
                try:
                    quantity = int(input(f'Enter quantity for {item_name}: '))
                    
                    if quantity > 0:
                        if item_name in cart:
                            cart[item_name] += quantity
                        else:
                            cart[item_name] = quantity
                        
                        print(f'Added {quantity} {item_name}(s) to cart')
                    else:
                        print("Please enter a positive quantity")
                except ValueError:
                    print("Invalid quantity. Please enter a number.")
            else:
                print(f"Invalid selection. Please choose a number between 1 and {len(item_list)}")
        except ValueError:
            print("Please enter a valid number")
            
    elif choice == "3":
        print('\n--- Cart Summary ---')
        
        if not cart:
            print("Your cart is empty")
            continue
            
        subtotal = 0
        for item_name, quantity in cart.items():
            price = items[item_name]
            item_total = price * quantity
            subtotal += item_total
            print(f"{item_name} x {quantity} = ₱{item_total}")
        
        vat = subtotal * 0.12
        total = subtotal + vat
        
        print(f"Subtotal: ₱{subtotal}")
        print(f"VAT (12%): ₱{vat:.2f}")
        print(f"Total: ₱{total:.2f}")
        
    elif choice == "4":
        print('Thank you for shopping with us!')
        break
        
    else:
        print('Invalid choice! Please enter a number between 1 and 4.')