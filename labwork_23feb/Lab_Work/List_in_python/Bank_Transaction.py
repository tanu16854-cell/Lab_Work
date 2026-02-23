# Bank Transaction Analyzer
# This program:
# 1. Calculates total balance
# 2. Finds largest withdrawal
# 3. Counts deposits greater than ₹10,000

#List of transactions
# Positive values = deposits, Negative values = withdrawals
transactions = [15000, -2000, 5000, -12000, 20000, -3000, 8000]

#Calculate total balance
total_balance = sum(transactions)

print("Total Balance:", total_balance)
print("--------------------------------------")

#Find largest withdrawal
# (largest withdrawal = most negative value)
withdrawals = []

for t in transactions:
    if t < 0:
        withdrawals.append(t)

if len(withdrawals) > 0:
    largest_withdrawal = min(withdrawals)   # smallest value = largest withdrawal
    print("Largest Withdrawal:", largest_withdrawal)
else:
    print("No withdrawals found")
print("--------------------------------------")
#Count deposits greater than ₹10,000
count_deposits = 0

for t in transactions:
    if t > 10000:
        count_deposits += 1

print("Deposits greater than ₹10,000:", count_deposits)
print("--------------------------------------")
