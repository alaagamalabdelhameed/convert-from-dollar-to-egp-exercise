def currency(dollar):
    egp =  dollar * 30.6044
    msg = ""
    if dollar > 1000:
        msg = "This is alot of money"
    return f"{dollar} Dollar is equal to {egp} EGP \n{msg}"


user_input = float(input("Enter amount of money in dollar: $"))
print(currency(user_input))

