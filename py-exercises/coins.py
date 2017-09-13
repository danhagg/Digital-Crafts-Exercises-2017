print("You have zero coins")
counter = 0
while True:

    cont = input("Would you like another coin? yes/no ").lower()
    while cont.lower() not in ("yes","no"):
        print("you entered an incorrect value")
        cont = input("Would you like another coin? yes/no > ").lower()
    if cont =='yes':
        counter += 1
        continue
    if cont == "no":
        print(str(counter))
        break
