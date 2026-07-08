def add_to_cart(cart_items, item_prices):
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    cart_items.append(item)
    item_prices.append(price)
    print(item, "added to cart.")

def view_cart_total(cart_items, item_prices):
    if not cart_items:
        print("Your cart is empty.")
        return
    print("\n--- Shopping Cart ---")
    for i in range(len(cart_items)):
        print(cart_items[i], "-", item_prices[i])
    total = sum(item_prices)
    print("Total Amount:", total)
    print("---------------------")

def shopping_project():
    cart_items = []
    item_prices = []
    while True:
        print("\n1. Add Item to Cart\n2. View Cart & Total\n3. Checkout & Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_to_cart(cart_items, item_prices)
        elif choice == "2":
            view_cart_total(cart_items, item_prices)
        elif choice == "3":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice!")

def main():
    shopping_project()

main()
