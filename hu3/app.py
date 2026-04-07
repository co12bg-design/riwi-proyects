from services import *
from archivos import *


inventory = []


while True:

    print("\n----- INVENTORY SYSTEM -----")
    print("1 Add product")
    print("2 Show inventory")
    print("3 Search product")
    print("4 Update product")
    print("5 Delete product")
    print("6 Statistics")
    print("7 Save CSV")
    print("8 Load CSV")
    print("9 Exit")

    option = input("Select option: ")

    if option == "1":

    # Validate name (letters only)
        while True:
            name = input("Name: ")
            if name.replace(" ", "").isalpha():
                break
            else:
                print("Name must contain only letters.")

    # Validate price (number, can include decimal)
        while True:
            price = input("Price: ")
            if price.replace(".", "", 1).isdigit():
                price = float(price)
                break
            else:
                print("Price must be a number.")

    # Validate quantity (integer only)
        while True:
            quantity = input("Quantity: ")
            if quantity.isdigit():
                quantity = int(quantity)
                break
            else:
                print("Quantity must be an integer.")

        add_product(inventory, name, price, quantity)
    elif option == "2":

        show_inventory(inventory)

    elif option == "3":

        name = input("Product name: ")
        product = search_product(inventory, name)

        if product:
            print(product)
        else:
            print("Not found")

    elif option == "4":

        name = input("Product name: ")
        price = float(input("New price: "))
        quantity = int(input("New quantity: "))

        update_product(inventory, name, price, quantity)

    elif option == "5":

        name = input("Product name: ")
        delete_product(inventory, name)

    elif option == "6":

        stats = stadistics(inventory)

        if stats:
            print(stats)
        else:
            print("Inventary empty")

    elif option == "7":

        ruta = input("File path: ")
        save_csv(inventory, ruta)

    elif option == "8":

        ruta = input("File path: ")
        products, issues = download_csv(ruta)

        if products:

            option2 = input("Overwrite inventory? (S/N): ")

            if option2.lower() == "s":
                inventory = products

            else:
                for p in products:
                    exist = search_product(inventory, p["nombre"])

                    if exist:
                        exist["quantity"] += p["quantity"]
                        exist["price"] = p["price"]
                    else:
                        inventory.append(p)

        print(f"Productos cargados: {len(products)}")
        print(f"Filas inválidas: {issues}")

    elif option == "9":

        print("see you later...")
        break

    else:

        print("Invalid option")