# Simple Bank System with Python
*This is a challenge of Data Engineering NTT DATA Bootcamp in [DIO](https://web.dio.me/).* It consists in a simple bank system based in three operations: withdraw money, deposit money and see account statement. The project also considers the currency as the brazilian one (Real).

# The Library
It was used only Pandas to generate statement table.

# Rules

## Withdraw rules
- There is a limit of 3 withdraws per day;
- A person can not withdraw if there is no money in account;
- A person can not withdraw if desired value is higher than account balance;
- A person can not withdraw if desired value is higher than R$ 500.00

## Deposit rule
- Deposit value can not be negative

## Statement rule
- No statement table should be showed if there weren't any previous withdraw or deposit operations;
- The table must describe the operation executed and its value;
- The values in table must be like R$ XX.XX (R$ 34.56, R$ 123.56)
