def display_items(cart):
    print("\nDisplaying Values")
    print(f"{'Key':<10}{'Value'}")
    for k, v in cart.items():
        print(f"{k:<10}{v}")
    print()

def search_item(cart):
    key = input("Enter key to search: ").strip()
    if key.isdigit():
        key = int(key)
        value = cart.get(key)
        if value:
            print(f"Found {value} item")
        else:
            print("I'm sorry, not in the cart")
    else:
        # search by value
        found = False
        for k, v in cart.items():
            if v.lower() == key.lower():
                print(f"Found {v} item")
                found = True
                break
        if not found:
            print("Key not found")

def remove_item(cart):
    key = input("Enter key to search: ").strip()
    if key.isdigit():
        key = int(key)
        value = cart.get(key)
        if value:
            del cart[key]
            print(f"The key {key} with value {value} has been deleted")
        else:
            print("I'm sorry, not in the cart")
    else:
        print("Key not found")

def change_item(cart):
    key = input("Enter key to search: ").strip()
    if key.isdigit():
        key = int(key)
        if key in cart:
            print(f"Found {cart[key]} item")
            new_value = input("Enter value: ")
            cart[key] = new_value
        else:
            print("I'm sorry, not in the cart")
    else:
        print("Key not found")

def main():
 
    cart = {
        0: "underwear",
        1: "tank top",
        2: "jacket"
    }

    print("You have 3 items in the cart")

    while True:
        action = input("What would you like to do [C]hange items [R]emove [D]isplay S[earch] ? ").strip().upper()

        if action == "D":
            display_items(cart)
        elif action == "S":
            search_item(cart)
        elif action == "R":
            remove_item(cart)
        elif action == "C":
            change_item(cart)
        elif action == "*":
            print("Bye")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()