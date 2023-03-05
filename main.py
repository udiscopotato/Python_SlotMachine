import random

MAX_LINES=3
MAX_BET = 100
MIN_BET = 1

ROWS=3
COLS=3


symbol_count={
    "A":3,
    "B":4,
    "C":5,
    "D":6
}

def get_SlotMachine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbol=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
            


def deposit():
    while True:
        amount=input("What would you like to deposit")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be more then Zero!")
        else:
            print("Enter a Valid Number")
    return amount


def get_numberOf_lines():
    while True:
        lines=input("what the number of lines you want to bet [1-"+str(MAX_LINES)+"]")
        if lines.isdigit():
            lines = int(lines)
            if 0 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a number between 1 to"+str(MAX_LINES))
        else:
            print("Enter a valid number")
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount should be between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a valid number")
    return bet

def main():
    balance=deposit()
    lines=get_numberOf_lines()
    while True:
        bet= get_bet()
        total_amount=lines*bet
        if total_amount > balance:
            print(f"Sorry you have insufficient balance {balance} and the required balance is {total_amount}")
        else:
            break
    
    remainig=balance-total_amount
    
    print(f" You're betting on {lines}lines , {bet} each \n total amount deduced from balance {total_amount} \n remaining balance {remainig}")
    


main()
    

