txns = [5000,-1200,-300,2500,-4500,800,50]

credits,debits =[],[]

total_credits =0
total_debits = 0

largest_debit =None

for amt in txns:
    if amt >= 0:
        credits.append(amt)
        total_credits += amt
    else:
        debits.append(amt)
        total_debits += amt
        if largest_debit is None or amt< largest_debit:
            largest_debit = amt

print("credits: ", credits, "total = " , total_credits)
print("debits: ", debits, "total = " , total_debits)
print("Net flow: ", total_debits + total_credits)
print("largest debit : ",largest_debit)

