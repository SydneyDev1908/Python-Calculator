def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("You can't divide by zero!")
    return x / y

def show_history(history):
    if not history:
        print("No history yet.")
    else:
        print("\nCalculation History:")
        for entry in history:
            print(entry)
    print()  # Blank line for readability

def main():
    history = []
    
    while True:
        print("\nWhat would you like to do?")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")
        print("5: Show History")
        print("6: Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '6':
            print("Goodbye!")
            break

        if choice == '5':
            show_history(history)
            continue

        if choice not in ['1', '2', '3', '4']:
            print("Invalid option. Please choose a valid number.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        if choice == '1':
            result = add(num1, num2)
            history.append(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            history.append(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            history.append(f"{num1} * {num2} = {result}")
        elif choice == '4':
            try:
                result = divide(num1, num2)
                history.append(f"{num1} / {num2} = {result}")
            except ValueError as e:
                print(e)
                continue

        print(f"Result: {result}")

if __name__ == "__main__":
    main()
