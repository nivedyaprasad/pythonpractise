Principal=float(input("principle = "))
Rate=float(input("rate = "))
Time=int(input("time in years = "))

simple_interest = Principal*Rate*Time//100
amount_payable = simple_interest + Principal

print ("simple interest = ", simple_interest)
print ("amount payable = ", amount_payable)
