import pandas as pd

options = """Select the desired operation:

1 = Make a withdraw
2 = Make a deposit
3 = See account statement
4 = Exit program

"""

MAX_WITHDRAW = 500.00
balance = 0.0
withdraw_num = 0
WITHDRAW_LIMIT = 3
operat = []
money = []

while True:
  print(f'Your current balance is R$ {balance:.2f}\n')
  operation = int(input(options))

  if operation == 1:
    if withdraw_num >= WITHDRAW_LIMIT:
      print("Error: you achieved withdraw limit for today\n")
    elif balance == 0:
      print("You don't have money to withdraw")
    else:
      value = float(input("Input the withdraw value: "))
      if value > balance:
        print("Error: you can not withdraw a balance higher than current balance\n")
      elif value > MAX_WITHDRAW:
        print(f"Error: you can not withdraw a balance higher than R$ {MAX_WITHDRAW:.2f} limit")
      elif round(value,2) > 0:
        balance -= value
        withdraw_num += 1
        money.append(f'R$ {value:.2f}')
        operat.append("Withdraw:")
      else:
        print("Invalid value or unknown error")
    print("")

  elif operation == 2:
    value = float(input("Input the deposit value: "))
    if round(value,2) > 0:
      balance += value
      money.append(f'R$ {value:.2f}')
      operat.append("Deposit:")
    else:
      print("Invalid value or unknown error")
    print("")

  elif operation == 3:
    statement = {'Operation':operat,'Value':money}
    statement = pd.DataFrame(statement)
    if (operat == []) or (money == []):
      print("No operations were made today")
    else:
      print(statement)
    print(f'\nFinal balance: R$ {balance:.2f}')
    print("")

  elif operation == 4:
    break

  else:
    print("Error: unknown operation\n")
    print("")