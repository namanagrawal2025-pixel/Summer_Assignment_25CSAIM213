def add_product(inventory):
    prod_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))
    inventory[prod_id] = {"Name": name, "Quantity": qty}
    print("Product added successfully!")

def update_quantity(inventory):
    prod_id = input("Enter Product ID: ")
    if prod_id in inventory:
        qty = int(input("Enter new total quantity: "))
        inventory[prod_id]["Quantity"] = qty
        print("Quantity updated.")
    else:
        print("Product not found.")

def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    for prod_id, details in inventory.items():
        print("ID:", prod_id, "| Name:", details["Name"], "| Quantity:", details["Quantity"])

def inventory_system():
    inventory = {}
    while True:
        print("\n1. Add Product\n2. Update Quantity\n3. View Inventory\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            update_quantity(inventory)
        elif choice == "3":
            view_inventory(inventory)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def main():
    inventory_system()

main()
