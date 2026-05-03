print("======BOOKKEEPING PROGRAM ======")
print("   1. Record Transaction")
print("   2. View transaction history")
print("   3. Remove transaction record")
print("   4. Exit program")

transaction = ""

def record_transaction():
    global transaction
    
    calendar = input("\nDate of transaction (YY/MM/DD): ")
    type_money = input("What type of transaction (Expense/Income): ")
    description = input("Description about transaction: ")
    while True:
        money_input = input("Amount used/received: ")
        if money_input.isdigit() and int(money_input) > 0:
            money = int(money_input)
            break
        else:
            print("Invalid input! Please enter correct input.")

    print("\nTransaction recorded!")
    print("Date:", calendar)
    print("Type:", type_money)
    print("Description:", description)
    print("Amount:", money)
    
    transaction += f"{calendar}, {type_money}, {description}, {money}\n"
    
while True:
    choice = int(input("\nChoose a number (1 - 4): "))

    if choice == 1:
        record_transaction()
    elif choice == 2:
        print("----- Transaction History ----- ")
        
        if not transaction:
            print("No transaction made yet")
        else:
            record = transaction.strip().split("\n")

            for index, number in enumerate(record, start=1):
                print(f"{index}. {number}")
