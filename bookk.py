transaction = []

def record_transaction():
    while True:
        calendar = input("Date of transaction (YYYY/MM/DD): ")
        if len(calendar) != 10:
            print("Invalid format! Ex. 2025-01-01")
            continue
        if calendar[4] != "/" or calendar[7] != "/":
            print("Invalid format! Ex. 2025-01-01")
            continue
        for i in range(len(calendar)):
            if i == 4 or i == 7:
                continue
            if calendar[i] < "0" or calendar[i] > "9":
                print("Invalid format! Numbers only! Ex. 2025-01-01")
                break
        else:
            break

    while True:
        type_money = input("What type of transaction (expense/income): ")
        if type_money == "expense" or type_money == "income":
            break
        else:
            print("Invalid input expense/income only!")
            
    description = input("Description about transaction: ")
    while True:
        money_input = input("Amount: ")
        if money_input == "":
            print("Invalid input!")
            continue
        for tax in money_input:
            if tax < "0" or tax > "9":
                print("Invalid input! Numbers only!")
                break
        else:
            money = int(money_input)
            if money <= 0:
                print("Invalid input must be greater than 0!")
                continue
            break
            
                
    print("Transaction recorded!")
    print("Date:", calendar)
    print("Type:", type_money)
    print("Description:", description)
    print("Amount:", money)
    
    transaction.append([calendar, type_money, description, money])
    
while True:
    print("======BOOKKEEPING PROGRAM ======")
    print("   1. Record Transaction")
    print("   2. View transaction history")
    print("   3. Remove transaction record")
    print("   4. Exit program")
    choice = (input("Choose a number (1 - 4): "))
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("Invalid input select a number from the choices!")
        continue
    choice = int(choice)
    
    if choice == 1:
        record_transaction()
        
        
    elif choice == 2:
        print("----- Transaction History ----- ")
        
        if not transaction:
            print("No transaction made yet")
        else:
            number = 1
            for index in transaction:
                print(f"{number} - {index[0]} - {index[1]} - {index[2]} - {index[3]}")
                number += 1
                
                
    elif choice == 3:
        print("----- Transaction History ----- ")
        
        if not transaction:
            print("No transaction made to remove yet")
        else:
            number = 1
            for index in transaction:
                print(f"{number} - {index[0]} - {index[1]} - {index[2]} - {index[3]}")
                number += 1
            while True:
                remove = input("Select a record number to remove/(Type exit to go back): ")
                if remove == "exit":
                    break
                if remove == "":
                    print("Invalid input! Empty space!")
                    continue
                for records in remove:
                    if records < "0" or records > "9":
                        print("Invalid input! Letter not allowed!")
                        break
                else:
                    remove = int(remove)
                    if remove < 1 or remove > len(transaction):
                        print("Invalid number! Please choose a record number to remove!")
                        continue
                    transaction.pop(remove - 1)
                    print(f"Removed record no.{remove} successfully! View transaction history to see.")
                    break