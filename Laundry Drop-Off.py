print("AQUA TIERA LAUNDRY SHOP")
from datetime import date
receipt_counter = 1

while True:
    print()
    today = date.today()
    print("Date: ", today)
    print()
    print("================Services================")
    print("1. Wash, Dry, fold")
    print("2. Dry Cleaning")
    print("3. Ironing and pressing")

    service = input("Enter your option: ")

    if service == "1":
        service = "Wash, Dry, Fold"
        rate = 50
    elif service == "2":
        service = "Dry Cleaning"
        rate = 80
    elif service == "3":
        service = "Ironing and pressing"
        rate = 100
    else:
        print("Invalid option, try again.")
        print()
        continue 
    print()
    print(service.center(40, "="))
    rate_text = (f"{rate} per kilo")
    print(rate_text.center(38, "="))

    name = input("Name: ")
    receipt_num = receipt_counter
    receipt_counter += 1

    while True:
        contact_num_customer = input("Contact number: ") 
        if contact_num_customer.isdigit() and len(contact_num_customer) == 11:
            break
        elif contact_num_customer.isdigit() and len(contact_num_customer) <= 11:
            print("Invalid contact number! It must be exactly 11 digits.\n")
        else:
            print("Invalid! enter again\n")
        
    print("Aqua Tiera Contact #: 09670166858 ")
    weight = float(input("Enter weight: ")) 
    print("Total amount: ", weight * rate)

    while True:
        rc = str(input("Do you want to print the receipt?(yes/no): "))
        if rc.lower() == "yes":
            print_receipt = True
            break
        if rc.lower() == "no":
            print_receipt = False
            break
        else:
            print("Invalid! please type yes or no")
    if not print_receipt:
        continue

    from datetime import date, timedelta
    future_date = today + timedelta(days=2) 
    
    print("\n")
    print("___________________________________________")
    print()
    print("             Aqua Tiera Laundry               ")
    print("Ilaya, Vamenta Blvd, Carmen, Cagayan De Oro City")
    print("   Aqua Tiera Contact #: 09670166858             ")
    print("___________________________________________")
    print()
    print("Date: ", today)
    print(f"Receipt Number: {receipt_num}")
    print("Customer name: ", name)
    print("Contact number: ", contact_num_customer)
    print("Pick-up date : ", future_date)
    print(f"Receipt Number: {receipt_num}")
    print()
    print(service.center(40, "="))
    rate_text = (f"{rate} per kilo")
    print(rate_text.center(38, "="))
    print("Total weight: ", weight, "kg")
    print("Rate per kilo: ", rate)
    print("Total amount: ₱", weight * rate)
    print("___________________________________________")
    print()
    print("Thank you for using our Laundry Services!")
    print() 
    print("Aqua Tiera Laundry Shop is not liable for unclaimed")
    print("clothes after 30 days.")
    print("___________________________________________")
    print()

    while True:
        another = input("Do you want to process another transaction? (yes/no): ")
        if another.lower() == "yes":
            another_trans = True
            break
        elif another.lower() == "no":
            another_trans = False
            break
        else:
            print("Invalid! please type yes/no")
    if not another_trans:
        print("Done transaction")
        break
