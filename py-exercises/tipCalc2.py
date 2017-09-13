bill = float(input("How much was the bill? "))
service = input("How was the service? 'Good', 'fair', or 'bad? '").lower()
num = int(input("How many people? "))

#make lowercase
def calcTip(bill, service, num):
    if service == "good":
        tip = bill * 0.2
        total = bill * 1.2
    elif service == "fair":
        tip = bill * 0.15
        total = bill * 1.15
    elif service == "bad":
        tip = bill * 0.1
        total = bill * 1.1

    each = total/num

    print("The tip equals {:.2f}".format(tip))
    print("The bill for each person equals {:.2f}".format(each))

calcTip(bill, service, num)
