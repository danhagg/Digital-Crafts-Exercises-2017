def gen_squares(nums):
    print("begin generator")
    for num in nums:
        yield num * num
        print("after yield")

def main():
    squares = gen_squares([1, 2, 3])
    print("made generator")
    for square in squares:
        print("control in the caller")
        print(square)
