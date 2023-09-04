import random

MAX_LINES = 3
MIN_LINES = 1
MAX_BET = 100
MIN_BET = 5

COLS = 3
ROWS = 3

items_slots = {"*": 2, "#": 4, "@": 6, "~": 10}

items_values = {"*": 5, "#": 4, "@": 3, "~": 2}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        item = columns[0][line]
        for column in columns:
            item_to_check = column[line]
            if item != item_to_check:
                break
        else:
            winnings += values[item] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_spin(rows, cols, items_slots):
    all_items = []
    for item, item_count in items_slots.items():
        for _ in range(item_count):
            all_items.append(item)

    columns = []
    for _ in range(cols):
        column = []
        current_items = all_items[:]
        for _ in range(rows):
            value = random.choice(current_items)
            current_items.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def depositMoney(balance):
    while True:
        answer = input("Would you like to deposit money?(Y/N)")
        if answer == "y":
            amount = input("Insert the desired amount: $")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    balance += amount
                    break
                else:
                    print("Amount must be greater than 0")
            else:
                print("Enter a valid number")
        elif answer == "n":
            break
    return balance


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
        amount = input(
            "Insert the desired amount you would like to bet on each line: $"
        )
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount to bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter a valid number")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"There's not enough money to bet that amount, your balance is: ${balance}"
            )
            break
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}"
    )

    slots = get_spin(ROWS, COLS, items_slots)
    print_slots(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, items_values)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = 0
    while True:
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break

        balance = depositMoney(balance)
        print(f"Current balance is ${balance}")
        balance += spin(balance)
        print(f"You left with ${balance}")


main()
