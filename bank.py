import bank_security_module as bsm


print("WELCOME TO THE BANK.")

while True:
    print("1. Create new Account")
    print("2. Login")
    print("3. Exit")
    try:
        user_input = int(input("> "))
        if user_input == 1:
            bsm.new_user()
        elif user_input == 2:
            name, login_credential = bsm.uname_check()
            password = bsm.pword_check(login_credential)
            break
        elif user_input == 3:
            exit(0)
        else:
            print("Not a valid input")
    except ValueError:
        print("Error.. Try again!")


print(f"Welcome, {name}")
while True:
    try:
        balance = bsm.account_info(name, login_credential)
        print("1. Check balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Logout")
        logged_in_user_input = int(input("> "))
        if logged_in_user_input == 1:
            print(f"Your current bank balance is ${balance}")
        elif logged_in_user_input == 2:
            deposit_amount = int(input("Enter amount you wish to deposit: "))
            bsm.money_deposit(login_credential, deposit_amount)
            print("Amount deposited successfully")
        elif logged_in_user_input == 3:
            withdraw_amount = int(input("Enter amount you wish to deposit: "))
            bsm.money_withdraw(login_credential, withdraw_amount)
            print("Amount withdrawn successfully")
        elif logged_in_user_input == 4:
            print("Logged out successfully!")
            exit(0)
        else:
            print("Not a valid input")

    except ValueError:
        print("Invalid input!")
        continue