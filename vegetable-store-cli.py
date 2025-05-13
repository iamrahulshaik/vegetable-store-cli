import datetime

vegetables = ["potato", "tomato", "onion", "carrot", "beans"]
quantity = [10, 20, 30, 40, 50]  
price = [10, 30, 40, 50, 20]  
get_price = [8, 25, 35, 45, 17]  
bill_history = []  
total_store_sales = 0
all_cart = []
total_sold = [0] * len(vegetables)

print("*" * 20, "Welcome to Vcube Store", "*" * 20, "\n")

while True:
    print("=" * 60)
    print("\t1. Owner")
    print("\t2. Customer")
    print("\t3. Exit")
    print("=" * 60)

    choose = int(input("Select one option: "))
    print()

    if choose == 3:
        print("Exiting store... Thank you!")
        break

    if choose == 1:
        while True:
            print("-" * 60)
            print("\t\tOwner Menu")
            print("-" * 60)
            print("1. View items")
            print("2. Add item")
            print("3. Remove item")
            print("4. Update price")
            print("5. Update quantity")
            print("6. View Bill History")
            print("7. Total store sales")
            print("8. Exit")
            print("-" * 60)

            user_choice = (input("Enter your choice: "))
            print()

            if user_choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                user_choice = int(user_choice)
            else:
                print("Invalid input! Please enter a number between 1 and 8.\n")
                continue 

            if user_choice == 1:
                print("-" * 60)
                print("Vegetables\t    Quantity (kg)\t   Price\t    get_price")
                print("-" * 60)
                for i in range(len(vegetables)):
                    print(f"{vegetables[i]}\t\t      {quantity[i]}\t\t           {price[i]}\t\t           {get_price[i]}")
                print("-" * 60) 
                print()

            elif user_choice == 2:
                item = input("Enter the item name: ")
                if item in vegetables:
                    print("Item already exists!")
                else:
                    vegetables.append(item)
                    price.append(int(input("Enter the selling price: ")))
                    get_price.append(int(input("Enter the buying price: ")))
                    quantity.append(int(input("Enter the quantity: ")))
                    total_sold.append(0)
                    print("Item added successfully!")
                print()

            elif user_choice == 3:
                item = input("Enter the item name to remove: ")
                if item in vegetables:
                    index = vegetables.index(item)
                    vegetables.pop(index)
                    quantity.pop(index)
                    price.pop(index)
                    print("Item removed successfully!")
                else:
                    print("Item not found!")
                print()

            elif user_choice == 4:
                item = input("Enter the item name to update price: ")
                if item in vegetables:
                    index = vegetables.index(item)
                    price[index] = int(input("Enter the selling price: "))
                    get_price[index] = int(input("Enter the new buying price: "))
                    print("Price updated successfully!")
                else:
                    print("Item not found!")
                print()

            elif user_choice == 5:
                item = input("Enter the item name to update quantity: ")
                if item in vegetables:
                    index = vegetables.index(item)
                    quantity[index] = int(input("Enter the new quantity: "))
                    print("Quantity updated successfully!")
                else:
                    print("Item not found!")
                print()

            elif user_choice == 6:
                print("\n" + "=" * 25 + " BILL HISTORY " + "=" * 25)
                print("No transactions yet." if not bill_history else "\n".join(bill_history))
                print()

            elif user_choice == 7:
                print("\n" + "=" * 20 + " FINAL STORE REPORT " + "=" * 20)
                print("\nItem\tTotal Sold (kg)\tTotal Sales (rs)\tProfit (rs)")
                print("-" * 60)

                total_profit = 0  
                for i in range(len(vegetables)):
                    if total_sold[i] > 0:
                        sales_amount = total_sold[i] * price[i]
                        cost_amount = total_sold[i] * get_price[i]
                        profit = sales_amount - cost_amount
                        total_profit += profit
                        print(f"{vegetables[i]}\t\t{total_sold[i]}\t\t{sales_amount} rs\t\t{profit} rs")

                print("\nTotal Store Sales:", total_store_sales, "rs")
                print("Total Profit:", total_profit, "rs")
                print("=" * 60)

            elif user_choice == 8:
                break

    if choose == 2:
        name = input("Enter your name: ")
        while True:
            num = input("Enter your phone number: ")
            if len(num) == 10 and num.isdigit():
                break   
        cart, weight, amount = [], [], []

        print("-" * 50)
        print("Vegetables\t    Quantity (kg)\t   Price")
        print("-" * 50)
        for i in range(len(vegetables)):
            print(f"{vegetables[i]}\t\t      {quantity[i]}\t\t        {price[i]}")
        print("-" * 50)
        print()

        while True:
            product = input("\nWhat do you want (type 'exit' to generate bill): ")
            if product.lower() == "exit":
                print("\nYour total cart value is:", sum(amount), "rs")
                print("=" * 50)
                customer_m = input("Do you want to modify your cart? (yes/no): ")
                print()

                if customer_m == "yes":
                    while True:
                        print("-" * 50)
                        print("Item\t\tQuantity (kg)\tPrice (rs)")
                        print("-" * 50)
                        for i in range(len(cart)):
                            print(f"{cart[i]}\t\t{weight[i]}\t\t{amount[i]}")
                        print("-" * 50)
                        print("Total Price:", sum(amount))
                        print("-" * 50)
                        print()
                        print("1. Add item")
                        print("2. Remove item")
                        print("3. Update quantity")
                        print("4. Exit")
                        customer_m1 = input("Select one option: ")

                        if customer_m1 == "1":
                           item_to_add = input("Enter the item name to add: ")
                           if item_to_add in vegetables:
                                index = vegetables.index(item_to_add)
                                quantity_to_add = int(input("Enter the quantity to add: "))

                                if quantity_to_add <= quantity[index]:
                                                
                                    cart.append(item_to_add)
                                    weight.append(quantity_to_add)
                                    new_bill = quantity_to_add * price[index]
                                    amount.append(new_bill)

                                                
                                    total_sold[index] += quantity_to_add
                                    # total_store_sales += new_bill

                                               
                                    quantity[index] -= quantity_to_add

                                    print("Item added successfully!")
                                else:
                                    print("Insufficient quantity available!")
                           else:
                                print("Item not available!")


                                    

                        if customer_m1 == "2":
                            item_to_remove = input("Enter the item name to remove: ")
                            if item_to_remove in cart:
                                index = cart.index(item_to_remove)
                                item_index = vegetables.index(item_to_remove)


                                quantity[item_index] += weight[index]


                                total_sold[item_index] -= weight[index]


                                total_store_sales -= amount[index]


                                cart.pop(index)
                                weight.pop(index)
                                amount.pop(index)
                                print(f"Item {item_to_remove} removed successfully!")
                            else:
                                print("Item not found in cart!")

                        elif customer_m1 == "3":
                            item_to_update = input("Enter the item name to update quantity: ")
                            if item_to_update in cart:
                                index = cart.index(item_to_update)
                                item_index = vegetables.index(item_to_update)

                                new_qty = int(input("Enter the new quantity: "))
                                available_stock = quantity[item_index] + weight[index]

                                if new_qty <= available_stock:

                                    quantity[item_index] = available_stock - new_qty


                                    total_sold[item_index] -= weight[index]
                                    total_sold[item_index] += new_qty


                                    weight[index] = new_qty
                                    new_amount = new_qty * price[item_index]


                                    total_store_sales -= amount[index] 
                                    total_store_sales += new_amount  

                                    amount[index] = new_amount
                                    print(f"Item {item_to_update} updated successfully!")
                                else:
                                    print("Not enough stock available!")
                            else:
                                print("Item not found in cart!")

                        elif customer_m1 == "4":
                            break

                break

            if product in vegetables:
                index = vegetables.index(product)
                qty = int(input("\nHow many kg do you want: "))
                if qty <= quantity[index]:
                    cart.append(product)
                    weight.append(qty)
                    bill = qty * price[index]
                    amount.append(bill)
                    total_sold[index] += qty
                    quantity[index] -= qty
                    print(f"Your bill for {qty} kg of {product} is {bill} rs.")
                else:
                    print(f"Item is out of stock, only {quantity[index]} kg is available.")
            else:
                print("Item not available.")

        total_store_sales += sum(amount)
        all_cart.append((cart, weight, amount))

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bill_data = f"""
Bill No: {len(bill_history) + 1}
Customer: {name} \nNumber: {num}\nDate: {current_time}\n
Item\t\tQuantity (kg)\tPrice (rs)\n---------------------------------------\n"""
        for i in range(len(cart)):
            bill_data += f"{cart[i]}\t\t{weight[i]}\t\t{amount[i]}\n"
        bill_data += f"\nTotal Price: {sum(amount)} rs\n{'-' * 40}\n"
        bill_history.append(bill_data)

        print("\n" + "*" * 15 + " BILL " + "*" * 15)
        print(bill_data)
