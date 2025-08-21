import slot_machine_module as smm
import bank_security_module as bsm


print(" ")
print("Welcome to the SLOT MACHINE GAME!")
print("Please login using your bank account")
name, login_credential = bsm.uname_check()
pword = bsm.pword_check(login_credential)
print("Logged in successfully!")
print(" ")
print(f"Welcome, {name}")

while True:
    balance = bsm.account_info(login_credential)
    print(f"Your bank balance is ${balance}")
    print(" ")
    user_bet = int(input("Enter your bet amount: $"))
    print(" ")
    bsm.money_withdraw(login_credential, user_bet)
    reward = smm.machine_emoji_selector(user_bet)
    bsm.money_deposit(login_credential, reward)

    continue_input = smm.user_continue()
    if continue_input == "y":
        continue
    elif continue_input == "n":
        exit(0)
    else:
        print("Invalid input. Try again ")


