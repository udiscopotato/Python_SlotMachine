
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

