# output file - Jay / 20% Fidel

from input import CURR_BALANCE, check_float_value

TITLE = ("\n************************************\n"
         "\t\t\t: ATM : \n"
         "************************************")
OPTIONS = ("\n Options:\n"
           "~~~~~~~~~~~~~~\n"
           "(1) Withdrawal\n"
           "(2) Deposit\n"
           "(3) BALANCE")


def print_title():
    print(TITLE)


def print_menu():
    print(TITLE)
    print(OPTIONS)


def end_screen():
    print(TITLE)
    print_balance()


def print_balance(balance):
    print(f"\nBalance: ${balance: .2f}")


def calc_withdrawal(withdrawal, total):
    if withdrawal > CURR_BALANCE:
        print("\nInsufficient funds.")
        exit()
    return total - withdrawal


def calc_deposit(deposit, total):
    return total + deposit


def choice(c, balance):
    print(f"Your balance is ${balance}\n")
    if (c == 1):
        # validate:
        withdrawal = check_float_value("Insert withdrawal amt: $")
        balance = calc_withdrawal(withdrawal, balance)

    elif (c == 2):
        deposit = check_float_value("Insert deposit amt: $")
        balance = calc_deposit(deposit, balance)

    print_menu()

    return balance

# end output file