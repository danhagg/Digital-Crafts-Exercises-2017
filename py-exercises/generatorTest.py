import memory_profiler
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print("List: Memory (Before): {}Mb".format(memory_profiler.memory_usage()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
        'id': i,
        'name': random.choice(names),
        'major': random.choice(majors)
        }

        result.append(person)
    return result

t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()

print("List: Memory (After): {}Mb".format(memory_profiler.memory_usage()))
print("Took {} Seconds".format(t2-t1))





print("Generator: Memory (Before): {}Mb".format(memory_profiler.memory_usage()))

def people_generator(num_people):
    for i in range(num_people):
        person = {
        'id': i,
        'name': random.choice(names),
        'major': random.choice(majors)
        }
        yield person

t3 = time.clock()
people = people_generator(1000000)
t4 = time.clock()

print("Generator: Memory (After): {}Mb".format(memory_profiler.memory_usage()))
print("Took {} Seconds".format(t4-t3))
