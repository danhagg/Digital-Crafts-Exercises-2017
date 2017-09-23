def func():
    yield 1
    yield 2
    yield 3

gen = func()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
