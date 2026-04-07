# Inventory Management System (Python)

## Overview
This project is a console-based Inventory Management System developed in Python.  
It allows users to manage products using CRUD operations, calculate inventory statistics, and store or load inventory data using CSV files.

The program is modularized into multiple files to improve code organization and maintainability.

---

## Features

### Product Management (CRUD)
The system allows the user to:
- Add a new product
- Show all products in the inventory
- Search for a product by name
- Update a product's price or quantity
- Delete a product from the inventory

### Inventory Statistics
The system calculates:
- Total units in inventory
- Total inventory value
- Most expensive product
- Product with the highest stock

### CSV Data Persistence

The program supports saving and loading inventory data.

Save CSV:
- Saves the current inventory to a CSV file
- Validates that the inventory is not empty
- Handles file writing errors

Load CSV:
- Loads products from a CSV file
- Validates file format and values
- Skips invalid rows
- Allows the user to overwrite or merge inventories

---

## Data Structure

The inventory is stored as a list of dictionaries.

## Project Structure

inventory_project/

app.py  
Main program that runs the menu and connects all functions.

servicios.py  
Contains the functions for inventory operations:
- agregar_producto
- mostrar_inventario
- buscar_producto
- actualizar_producto
- eliminar_producto
- calcular_estadisticas

archivos.py  
Contains functions related to CSV files:
- guardar_csv
- cargar_csv

README.md  
Project documentation.

diagrama_flujo.png / PDF  
Flowchart of the system.

---

## CSV Format

The CSV file must follow this structure:

nombre,precio,cantidad
Laptop,1200,5
Mouse,25,20
Keyboard,80,10

Rules:
- The file must contain 3 columns
- The header must be: nombre,precio,cantidad
- precio must be a float
- cantidad must be an integer
- Negative values are not allowed

Invalid rows are skipped and counted.

---

## Menu Options

1 Add product  
2 Show inventory  
3 Search product  
4 Update product  
5 Delete product  
6 Statistics  
7 Save CSV  
8 Load CSV  
9 Exit  

The program runs in a loop until the user selects Exit.

---

## Error Handling

The system handles the following errors:

- Invalid menu options
- Non-numeric input values
- Missing files
- Invalid CSV format
- File encoding errors
- File writing errors

All errors are handled using try/except blocks so the program does not crash.

---

## Requirements

Python 3.x

The project only uses the built-in Python library:
csv

No external libraries are required.

---

## How to Run

1. Open a terminal in the project folder.

2. Run the program with:

python app.py

3. Use the menu to interact with the inventory system.

---

## Flowchart

The project includes a flowchart that describes the complete program flow, including:

- Main menu logic
- CRUD operations
- CSV save process
- CSV load process
