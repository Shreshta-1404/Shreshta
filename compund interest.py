def calculate_compound_interest(principle,rate,time):
    """
    :param principle:the initial amount of money(float or int):
    :param rate:the annual interest rate(float or int):
    :param time:the number of period of the money is investead for(float or int):
    :return:the compound interest(float).
    """
    # convert rate from percentage to decimal
    rate_decimal=rate/100
    #calculate the compound interest
    amount=principle*(1+rate_decimal)**time
    compound_interest=amount-principle
    
    return compound_interest
# Input Values
principle=float(input("Enter the principle amount:"))
rate=float(input("Enter the annual interest rate in percentage:"))
time=float(input("Enter the number of periods:"))
#calculate compound interest
interest=calculate_compound_interest(principle,rate,time)
#outputthe result
print(f"The compound interest is:{interest:.2f}")
