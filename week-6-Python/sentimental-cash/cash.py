def get_cents():
    while True:
        try:
            dollars = float(input("Troco a devolver? (change value): "))
            cents = int(dollars * 100)  # Converter dólares em centavos

            if cents >= 0:
                break
        except ValueError:
            pass

    return cents

def calculate_quarters(cents):
    return cents // 25

def calculate_dimes(cents):
    return cents % 25 // 10

def calculate_nickels(cents):
    return cents % 25 % 10 // 5

def calculate_pennies(cents):
    return cents % 25 % 10 % 5

def main():
    cents = get_cents()

    quarters = calculate_quarters(cents)
    dimes = calculate_dimes(cents)
    nickels = calculate_nickels(cents)
    pennies = calculate_pennies(cents)

    coins = quarters + dimes + nickels + pennies

    print(coins)

if __name__ == "__main__":
    main()
