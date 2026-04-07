import csv
import os


def save_csv(inventory, route, include_header=True):
    """save the inventory information to a CSV file."""

    if not inventory:
        print("inventory empty, process not complet.")
        return

    try:
        with open(route, "w", newline="") as file:
            writer = csv.writer(file)

            if include_header:
                writer.writerow(["name", "price", "quantity"])

            for p in inventory:
                writer.writerow([p["name"], p["price"], p["quantity"]])

        print(f"inventory saved to: {route}")

    except Exception as e:
        print("Error saving file:", e)


def download_csv(route):
    """submits the inventory information from a CSV file."""

    products = []
    issues = 0

    try:
        with open(route, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            header = next(reader)

            if header != ["name", "price", "quantity"]:
                raise ValueError("inválid header, expected: name, price, quantity")

            for row in reader:

                if len(row) != 3:
                    issues += 1
                    continue

                try:
                    name = row[0]
                    price = float(row[1])
                    quantity = int(row[2])

                    if price < 0 or quantity < 0:
                        raise ValueError

                    products.append({
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    })

                except:
                    issues += 1

    except FileNotFoundError:
        print("File not found.")
    except UnicodeDecodeError:
        print("Error decoding file.")
    except Exception as e:
        print("Error:", e)

    return products, issues