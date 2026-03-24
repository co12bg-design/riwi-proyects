
print ("Welcome to the inventory")

#in this line we define the variable for the product name and validate that it only contains letters using the isalpha() method, if the input is invalid, it will prompt the user to enter the product name again until a valid input is provided
Name= input ("product Name:")
#we use a while loop to check if the input is valid, if not, it will print an error message and ask for the input again until a valid name is entered
while not Name.isalpha():
    print("invalid name")  
    Name=input("product Name:").strip()
#we define the variable for the product price and validate that it is a positive number, if the input is invalid, it will prompt the user to enter the product price again until a valid input is provided
    price=float(input("Product Price: "))
while not price > 0:
    print("invalid price")
    price=float(input("Product Price: "))
    
#we define the variable for the product quantity and validate that it is a positive integer between 1 and 999, if the input is invalid, it will prompt the user to enter the product quantity again until a valid input is provided
quantity=int(input("Product Quantity: "))
while not quantity in range(1, 1000):
  print("invalid quantity")
  quantity=int(input("Product Quantity: "))

#we define the variable for the total cost and calculate it by multiplying the price by the quantity, then we print out all the information about the product including its name, price, quantity, and total cost in a formatted string
costo_total= price * quantity

print(f"Product Name: {Name}!Product Price: {price}!Product Quantity: {quantity}!Total cost: {costo_total}")

#this program is a simple inventory management system that allows the user to input the name, price, and quantity of a product, while ensuring that the inputs are valid. It then calculates the total cost of the product based on the price and quantity and displays all the information in a formatted manner.
