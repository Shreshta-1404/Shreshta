def calculate_compound_interest(principle,rate,time)
# convert rate from percentage to decimal
rate_decimal=rate/100
#calculate the compound interest
amount=principal*(1+rate_decimal)**time
compound_interest=amount -principle
return compond_interest
# Input Values
principle=float(input("Enter the principal amount:"))
rate=float(input("Enter the annual interest rate in percentage:"))
           time=float(input("Enter the number of periods:"))
           #calculate compound interest
           interest=calculate_compond_interest(principle,rate,time)
