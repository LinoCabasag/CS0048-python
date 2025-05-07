'''
Requirements
- display Menu
- allows repeated items until exit
- calculate total cost with 10 % discout
- do not use array, list 
- use if-elif for choices
'''

print('\n--- Welcome to Python Restaurant --- ')
print('\n--- Your Order --- ')

while True: 
    totalBalanceCost = 0
    for m in range (100):
        print('\nMenu: ')
        print('\t1. Burger - ₱120 ')
        print('\t2. Pizza - ₱300 ')
        print('\t3. Pasta - ₱250 ')
        print('\t4. Fries - ₱80 ')
        print('\t5. Exit.')

        choice = input('Enter Product no, of choice: ')
        if choice == "1":
            totalBalanceCost += 120.0 
            print('Added Burger to your Cart')
        elif choice == "2":
            totalBalanceCost += 300.0
            print('Added Pizza to your Cart')
        elif choice == "3":
            totalBalanceCost += 250.0
            print('Added Pasta to your Cart')
        elif choice == "4":
            totalBalanceCost += 80.0 
            print('Added Fries to your Cart')
        elif choice == "5":
            print('Thank you for shopping with us!')
            break
        else:
            print('Invalid Order!')
            

    print ('\t   --- Order Summary ---\n')

    if totalBalanceCost > 500.0:
        discountcost = totalBalanceCost - (totalBalanceCost* .10)
        print ( '\t   Total Before Discount: ₱',totalBalanceCost, '\n\t   Total After Discout:   ₱' , discountcost)
        break
    elif totalBalanceCost <= 500.0:
        print ('\t   Total: \t₱',totalBalanceCost)
        break