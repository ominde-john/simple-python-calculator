from datetime import datetime

history = []


def show_menu():
    print("\n===== PYTHON CALCULATOR & UNIT CONVERTER =====")
    print("1. Basic calculator")
    print("2. Unit converter")
    print("3. View history")
    print("4. Clear history")
    print("5. Exit")


def get_number(prompt):
    
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid number. Please enter a value such as 12 or 3.5.")


def record_history(entry_type, details):
    history.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": entry_type,
        "details": details,
    })


def basic_calculator():
    print("\n--- BASIC CALCULATOR ---")
    first_number = get_number("Enter the first number: ")
    operator = input("Choose an operator (+, -, *, /): ").strip()
    second_number = get_number("Enter the second number: ")

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            print("Cannot divide by zero!")
            return
        result = first_number / second_number
    else:
        print("Invalid operator. Choose +, -, *, or /.")
        return

    display_result = int(result) if result.is_integer() else result
    print(f"Result: {display_result}")
    record_history("Calculation", f"{first_number:g} {operator} {second_number:g} = {display_result}")


def convert_temperature():
    print("\n--- TEMPERATURE CONVERTER ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choice = input("Choose a conversion: ").strip()
    value = get_number("Enter the temperature: ")

    conversions = {
        "1": (value * 9 / 5 + 32, "°C", "°F"),
        "2": ((value - 32) * 5 / 9, "°F", "°C"),
        "3": (value + 273.15, "°C", "K"),
        "4": (value - 273.15, "K", "°C"),
        "5": ((value - 32) * 5 / 9 + 273.15, "°F", "K"),
        "6": ((value - 273.15) * 9 / 5 + 32, "K", "°F"),
    }

    if choice not in conversions:
        print("Invalid conversion choice.")
        return

    result, source_unit, target_unit = conversions[choice]

    # Reject temperatures below absolute zero.
    if (source_unit == "K" and value < 0) or (target_unit == "K" and result < 0):
        print("That temperature is below absolute zero and is not physically valid.")
        return

    print(f"Result: {value:g} {source_unit} = {result:.2f} {target_unit}")
    record_history("Temperature conversion", f"{value:g} {source_unit} = {result:.2f} {target_unit}")


def convert_distance():
    print("\n--- DISTANCE CONVERTER ---")
