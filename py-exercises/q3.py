"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

for x in range(1,21):
    for y in range(40,10000):
        print(divmod(x,y))
