name = input("Please enter a filename: ")+'.txt'

with open(name, 'w') as f:
    contents = f.write(input("Pleae enter some text: "))
    print(contents)
