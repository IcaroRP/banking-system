import time

money = 0
limit = 500
balance = 0
log = ""
limit_withdraw = 0
WITHDRAW_LIMIT = 3

while True:

# Menu inicial
    print('''
=============== M A Z E B A N K ===============
                 OF LOS SANTOS

                Choose a service
                1 - Deposit
                2 - Withdraw
                3 - Transaction Log
                4 - Exit

===============================================
    ''')

    user = input('Your choice: ')

# Opção de Deposito
    if user == '1':
        print('''
=============== Welcome: User =================
            
How much you want to deposit?
    ''')
        
        money = float(input('R$ '))

        if money > 0:  
            balance += money
            log += f'Deposit: R$ {money:.2f}\n'
            print('\nOperation successfully! Returning to the main menu.')
            time.sleep(3)
        else:
            print('\nInvalid operation. The entered value is incorrect.')
            time.sleep(3)

# Operação de Saque
    elif user == '2':
        print('''
=============== Welcome: User =================
            
How much you want to withdraw?
    ''')
        
        money = float(input('R$ '))

        exceeded_balance = money > balance
        exceeded_limit = money > limit
        exceeded_withdraw = limit_withdraw >= WITHDRAW_LIMIT

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

    elif user == '3':
        print('''
=============== Welcome: User =================
            
Your transaction history:
    ''')
        print('There are no logs of bank transactions in this account.' if not log else log)
        print(f'Balance: R$ {balance:.2f}\n')
        print('Returning to the main menu.')
        time.sleep(5)

    elif user == '4':
        break

    else:
        print('Invalid operation, please reselect the desired operation.')
        time.sleep(3)
