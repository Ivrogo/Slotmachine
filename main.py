MAX_LINES = 3
MIN_LINES = 1
MAX_BET = 100
MIN_BET = 5


def depositMoney():
    while True:
        amount = input("Insert the desired amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Enter a valid number")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet ("
            + str(MIN_LINES)
            + " - "
            + str(MAX_LINES)
            + ")? "
        )
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                break
            else:
                print(
                    "The number of lines must be in between "
                    + str(MIN_LINES)
                    + " and "
                    + str(MAX_LINES)
                )
        else:
            print("Enter a valid number for the lines")

    return lines


def get_bet():
    while True:
        amount = input("Insert the desired amount you would like to bet: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(
                    "Amount to bet must be in between "
                    + str(MIN_BET)
                    + " and "
                    + str(MAX_BET)
                )
        else:
            print("Enter a valid number")

    return amount


def main():
    balance = depositMoney()
    lines = get_number_of_lines()
    print(balance, lines)


main()
