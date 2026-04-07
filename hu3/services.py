"""
inventory´s services: CRUD y ataditics
"""

def add_product (inventory, name, price, quantity):
    """
    It adds a product to the inventory.

    Parameters:
    inventory (list): list of products
    name (str): product name
    price (float): product price
    quantity (int): product quantity

    Returns:
    None
    """
    product = {"name": name, "price": price, "quantity": quantity}
    inventory.append(product)


def show_inventory(inventory):
    """Display all products in the inventory."""

    if not inventory:
        print("Inventario empty.")
        return

    for p in inventory:
        print(f"{p['name']} | price: {p['price']} | Quantity: {p['quantity']}")


def search_product(inventory, name):
    """
    Searches for a product by name.

    Returns:
    dict or None
    """

    for p in inventory:
        if p["name"].lower() == name.lower():
            return p
    return None


def update_product(inventory, name, new_price=None, new_quantity=None):
    """Updates the price or quantity of a product."""

    producto = search_product(inventory, name)

    if producto:
        if new_price is not None:
            producto["price"] = new_price

        if new_quantity is not None:
            producto["quantity"] = new_quantity

        print("Product updated successfully.")
    else:
        print("Product not found.")


def delete_product(inventory, name):
    """Deletes a product from the inventory."""

    producto = search_product(inventory, name)

    if producto:
        inventory.remove(producto)
        print("Product deleted successfully.")
    else:
        print("Product not found.")


def stadistics(inventory):
    """
    Calculate inventory statistics: total units, total value, most expensive product, product with highest stock.

    Returns:
    dict with metrics
    """

    if not inventory:
        return None

    subtotal = lambda p: p["price"] * p["quantity"]

    total_units = sum(p["quantity"] for p in inventory)
    total_value = sum(subtotal(p) for p in inventory)

    most_expensive_product = max(inventory, key=lambda p: p["price"])
    product_highest_stock = max(inventory, key=lambda p: p["quantity"])

    return {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive_product": (most_expensive_product["name"], most_expensive_product["price"]),
        "product_highest_stock": (product_highest_stock["name"], product_highest_stock["quantity"])
    }