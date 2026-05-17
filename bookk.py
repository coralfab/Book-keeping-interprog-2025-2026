import records
while True:
    print("====== SIMPLE BOOKKEEPING PROGRAM ======")
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
        from records import record_transaction
        record_transaction()
 
       
    elif choice == 2:
        while True:
            print("----- Transaction History ----- ")
           
            if not records.transaction:
                print("No transaction made yet")
            else:
                number = 1
                for index in records.transaction:
                    print(f"{number} - {index[0]} - {index[1]} - {index[2]} - {index[3]}")
                    number += 1


            view = input("Select a record number to view/(Type exit to go back): ")


            if view == "exit":
                break
            if view == "Exit":
                break


            if view == "":
                print("Invalid input! Empty space!")
                continue


            for v in view:
                if v < "0" or v > "9":
                    print("Invalid input! Numbers only!")
                    break
            else:
                view = int(view)
                if view < 1 or view > len(records.transaction):
                    print("Invalid number!")
                    continue


                record = records.transaction[view - 1]
                print("--- Record Details ---")
                print("Date:", record[0])
                print("Type:", record[1])
                print("Description:", record[2])
                print("Amount:", record[3])
                print("----------------------")


                while True:
                    back = input("Do you want to go back to main menu? (Y/N): ")
                    if back == "Y" or back == "y":
                        break
                    elif back == "N" or back == "n":
                        break
                    else:
                        print("Invalid input! Enter Y or N: ")


                if back == "Y" or back == "y":
                    break
               
               
    elif choice == 3:
        print("----- Transaction History ----- ")
       
        if not records.transaction:
            print("No transaction made to remove yet")
        else:
            number = 1
            for index in records.transaction:
                print(f"{number} - {index[0]} - {index[1]} - {index[2]} - {index[3]}")
                number += 1
            while True:
                remove = input("Select a record number to remove/(Type exit to go back): ")
                if remove == "exit":
                    break
                if remove == "Exit":
                    break
                if remove == "":
                    print("Invalid input! Empty space!")
                    continue
                for records.transaction in remove:
                    if records.transaction < "0" or records.transaction > "9":
                        print("Invalid input! Letter not allowed!")
                        break
                else:
                    remove = int(remove)
                    if remove < 1 or remove > len(records.transaction):
                        print("Invalid number! Please choose a record number to remove!")
                        continue
                    records.pop(remove - 1)
                    print(f"Removed record no.{remove} successfully! View transaction history to see.")
                    break


    elif choice == 4:
        if not records.transaction:
            print("Exiting program...")
            break
        else:
            while True:
                confirm = input("Are you sure you want to exit? Your saved transaction records will be gone! (Y/N): ")
               
                if confirm == "Y" or confirm == "y":
                    print("Exiting program...")
                    break
               
                elif confirm == "N" or confirm == "n":
                    print("Exit cancelled.")
                    break
                else:
                    print("Invalid input! Please enter Y or N.")
           
            if confirm == "Y" or confirm == "y":
                break

        
            
