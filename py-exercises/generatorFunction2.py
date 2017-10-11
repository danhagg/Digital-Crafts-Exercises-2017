def gen_squares(nums):
    print("begin generator") #3
    for num in nums:
        yield num * num #4 yields its first value "1" in for loop
        print("after yield") #5 then flips back to caller

def main():
    #1 we make the generator "no gen_squares code is run"
    squares = gen_squares([1, 2, 3])
    print("made generator")
    #2 the for loop calls __next__ on generator and goes to gen_squares
    for square in squares:
        print("control in the caller") #6 print this
        #7 print the square of first yield, then goes to next iteartion of this for loop... ie #2 again then over to yield again #4
        print(square)

main()
