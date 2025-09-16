


USD_TO_INR = 83.02    # Indian Rupee
USD_TO_GBP = 0.76     # British Pound
USD_TO_CNY = 7.28     # Chinese Yuan

def convert_currency(dollar):
    """Convert dollar to INR, GBP, CNY"""
    inr = dollar * USD_TO_INR
    gbp = dollar * USD_TO_GBP
    cny = dollar * USD_TO_CNY
    return inr, gbp, cny

print("Dollar ($)\tIndian Rupee (R)\tBritish Pound (£)\tChina Yuan (Y)")

while True:
    user_input = input("Enter dollar ($) (* to exit): ")

    if user_input == "*":
        print("Bye")
        break

  
    dollars = user_input.split("@")

    for d in dollars:
        d = d.strip()
        if d.isdigit():
            d = float(d)
            inr, gbp, cny = convert_currency(d)
            print(f"{d:<15}{inr:<20.2f}{gbp:<20.2f}{cny:<20.2f}")
        else:
            print(f"Invalid input: {d}")