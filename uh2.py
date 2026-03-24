from itertools import product
from py_compile import main


print ("order management system")
#list to store products    
inventory = []

#function to display menu and handle user input
def menu():
 #cicle to display menu until user chooses to exit
 while True:     
        print("1. Add product")
        print("2. View inventory")
        print("3. Statistics")
        print("4. Exit")
        print("choose an option:")
        choice = input()
        
        if  choice == "1":
                        print("add product")
#user input for product details and defining a product as a dictionary and adding it to the inventory list
                        name = input("name: ")
                        price = float(input("price: "))
                        quantity = int(input("quantity: "))
                        product = {"name": name, "price": price, "quantity": quantity}
                        inventory.append(product)
                        print("product added successfully")
#this option allows the user to view the inventory by iterating through the inventory list and printing the details of each product. If the inventory is empty, it will print a message indicating that the inventory is empty.                
        elif choice == "2":
                        print("view inventory")
                        for product in inventory:
                            print(f"Product: {product['name']}|{product['price']}|{product['quantity']}")
                            if not inventory:
                                print("inventory is empty")
#this calculates the total inventory value by summing the product of price and quantity for each product in the inventory. It also counts the number of products in the inventory and prints both statistics to the user.
        elif choice == "3":
                        print("statistics")
                        total_value = sum(product["price"] * product["quantity"] for product in inventory)
                        print(f"total inventory value: {total_value}")          
                        product_length = len(inventory)
                        print(f"number of products: {product_length}")  
            
        elif choice == "4":
                 print("See you later!")
                 break
        else: print("Invalid option. Please try again.")             
      
menu()


