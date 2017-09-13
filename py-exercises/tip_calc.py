bill = float(input("How much was the bill? "))
service = input("How was the service? 'Good', 'fair', or 'bad? '").lower()

#make lowercase
def calcTip(bill, service):
    if service == "good":
        tip = bill * 0.2
        total = bill * 1.2
    elif service == "fair":
        tip = bill * 0.15
        total = bill * 1.15
    elif service == "bad":
        tip = bill * 0.1
        total = bill * 1.1

    print("The tip equals {:.2f}".format(tip))
    print("The bill equals {:.2f}".format(total))

calcTip(bill, service)
