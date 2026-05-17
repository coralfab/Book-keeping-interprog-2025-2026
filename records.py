transaction = []
def record_transaction():
    while True:
        while True: # Will ask the date of the transaction
            calendar = input("Date of transaction (YYYY/MM/DD): ")
            if len(calendar) != 10:
                print("Invalid format! Ex. 2025/01/01")
                continue
           
            if calendar[4] != "/" or calendar[7] != "/":
                print("Invalid format! Ex. 2025/01/01")
                continue
           
            for i in range(len(calendar)):
                if i == 4 or i == 7:
                    continue
                if calendar[i] < "0" or calendar[i] > "9":
                    print("Invalid format! Numbers only! Ex. 2025/01/01")
                    break
            else:
                break
           
        while True: #Will ask what type of transaction was received
            type_money = input("What type of transaction (expense/income): ")
            if type_money == "expense" or type_money == "income":
                break
           
            if type_money == "Expense" or type_money == "Income":
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
        print("=====================")      
        print("Transaction recorded!")
        print("Date:", calendar)
        print("Type:", type_money)
        print("Description:", description)
        print("Amount:", money)
        print("=====================")
       
        transaction.append([calendar, type_money, description, money])
        print("Successfully recorded!")
        while True:
            back = input("Do you want to record another transaction? (Y/N): ")
       
            if back == "Y" or back == "y":
                break  
       
            elif back == "N" or back == "n":
                return  
       
            else:
                print("Invalid input! Enter Y or N:")
