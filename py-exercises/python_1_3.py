nameSubject = input("Please provide two values 'x' and 'y' to satisfy the following question.\n You may seperate the values with a space\n Person x's favorite subject is y ")
val = nameSubject.split()

print(val[0] + ' favorite subject is ' + val[1])
