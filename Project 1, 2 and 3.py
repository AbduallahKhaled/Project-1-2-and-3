#Project 1 : Determine Course Grade and Pass/Fail Status
def determine_grade(degree):
    if degree >= 90:
        return "A", "Pass"
    elif degree >= 80:
        return "B", "Pass"
    elif degree >= 70:
        return "C", "Pass"
    elif degree >= 60:
        return "D", "Pass"
    else:
        return "F", "Fail"

degree = float(input("Enter your course degree (0-100): "))
grade, status = determine_grade(degree)

print(f"Grade: {grade}")
print(f"Status: {status}")


# Project 2: Check Divisibility by 3 and 2
def check_divisibility(number):
    if number % 3 == 0:
        return "The number is divisible by 3."
    elif number % 2 == 0:
        return "The number is not divisible by 3 but is divisible by 2."
    else:
        return "The number is not divisible by 3 or 2."

number = int(input("Enter an integer number: "))
result = check_divisibility(number)
print(result)


# Project 3: Coffee Shop Order and Receipt
def display_menu(menu):
    print("Welcome to the Coffee Shop!")
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

def calculate_total_cost(menu, drink, quantity):
    if drink in menu:
        price = menu[drink]
        total_cost = price * quantity
        return price, total_cost
    else:
        return None, None

menu = {
    "Espresso": 5.0,
    "Latte": 6.0,
    "Cappuccino": 6.5,
    "Americano": 4.5
}

display_menu(menu)

drink = input("Please enter the drink you want to order: ")
quantity = int(input("Enter the quantity: "))

price, total_cost = calculate_total_cost(menu, drink, quantity)

if total_cost is not None:
    print("\n--- Receipt ---")
    print(f"Drink: {drink}")
    print(f"Price per item: ${price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total amount to pay: ${total_cost:.2f}")
else:
    print("Sorry, we do not have that drink on the menu.")
