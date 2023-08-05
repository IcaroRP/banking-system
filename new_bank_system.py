import textwrap, time

def menu():
    # Menu inicial
    menu = """\n
=============== M A Z E B A N K ===============
                 OF LOS SANTOS

                Choose a service
                1 - Deposit
                2 - Withdraw
                3 - Transaction Log
                4 - Create New Account
                5 - Users list
                6 - Create New User
                7 - Exit

===============================================
Choose a option:
    """
    return input(textwrap.dedent(menu)) # Modulo textwrap pode ser usado apra quebra automaticad de linha e formatação de texto simples. O dedent é usado para remover qualquer espaço em branco inicial

def deposit(balance, money, log, /):
    if money > 0:  
            balance += money
            log += f'Deposit: R$ {money:.2f}\n'
            print('\nOperation successfully! Returning to the main menu.')
            time.sleep(3)
    else:
            print('\nInvalid operation. The entered value is incorrect.')
            time.sleep(3)
    return balance, log

def withdraw(*, balance, money, log, limit, limit_withdraw, withdraw_limit):
     exceeded_balance = money > balance
     exceeded_limit = money > limit
     exceeded_withdraw = limit_withdraw >= withdraw_limit
     
     if exceeded_balance:
            print('\nOperation failed. You do not have money in your account.')
            time.sleep(3)
     elif exceeded_limit:
            print('\nOperation failed. Withdrawal amount exceeded account limit.')
            time.sleep(3)
     elif exceeded_withdraw:
            print('\nOperation failed. Maximum withdrawals have been exceeded.')
            time.sleep(3)
     elif money > 0:
            balance -= money
            log += f'Withdraw: R$ {money:.2f}\n'
            limit_withdraw += 1
            print('\nOperation successfully! Returning to the main menu.')
            time.sleep(3)

     else:
            print('\nOperation failed. The entered value is invalid.')
            time.sleep(3)
     return balance, log

def show_log(balance, /, *, log):
      print('There are no logs of bank transactions in this account.' if not log else log)
      print(f'Balance: R$ {balance:.2f}\n')
      print('Returning to the main menu.')
      time.sleep(5)

def new_users(users):
      cpf = input("CPF(Only numbers): ")
      user = filter_users(cpf, users)

      if user:
            print("\nThere is already a user with this CPF.")
            time.sleep(5)
            return
      
      name = input("Enter your full name: ")
      birthday = input("Inform your birthday (dd-mm-aaaa): ")
      address = input("inform the address (Street, Number - District - City/Estate): ")

      users.append({"name": name, "birthday": birthday, "cpf": cpf, "address": address})
      print("User successfully created!")
      time.sleep(5)

def filter_users(cpf, users):
      filtered_users = [user for user in users if users["cpf" == cpf]]
      return filtered_users[0] if filtered_users else None

def create_account(agency, account_number, users):
      cpf = input("Enter the user's CPF: ")
      user = filter_users(cpf, users)

      if user:
            print("\nAccount successfully created!")
            return {"agency": agency, "account_number": account_number, "user": user}
      print("\nUser not found, account creation flow closed!")
      time.sleep(5)

def list_accounts(accounts):
      for account in accounts:
            line = f"""\
                Agency:\t{account['agency']}
                A/C:\t{account['account_number']}
                Owner:\t{account['user']['name']}
            """
            print("=" * 47)
            print(textwrap.dedent(line))
            time.sleep(5)

def main():
    WITHDRAW_LIMIT = 3
    AGENCY = "0001"

    money = 0
    limit = 500
    log = ""
    balance = 0
    limit_withdraw = 0
    users = []
    accounts = []
    
    while True:
        user_option = menu()

        if user_option == "1":
            print(
'''
=============== Welcome: User =================
            
How much you want to deposit?
''')
            money = float(input('R$ '))
            
            balance, log = deposit(balance,money,log)
        elif user_option == '2':
            print(
'''
=============== Welcome: User =================
            
How much you want to withdraw?
''')
        
            money = float(input('R$ '))

            money, log = withdraw(
                balance=balance,
                money=money,
                log=log,
                limit=limit,
                limit_withdraw=limit_withdraw,
                withdraw_limit=WITHDRAW_LIMIT,
                )
        elif user_option == '3':
            print(
'''
=============== Welcome: User =================
            
Your transaction history:
''')
            show_log(balance, log=log)

        elif user_option == '4':
              account_number = len(accounts) + 1
              account = create_account(AGENCY, account_number, users)

              if account:
                    accounts.append(account)
        
        elif user_option == '5':
              list_accounts(accounts)

        elif user_option == '6':
              new_users(users)
        elif user_option == '7':
              break

main()
