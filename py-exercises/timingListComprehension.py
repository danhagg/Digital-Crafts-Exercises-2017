import memory_profiler
import time


print("For loop list (Before): {}Mb".format(memory_profiler.memory_usage()))

t3 = time.clock()
a = []
for b in range(1,10000000):
     a.append(b*b)
t4 = time.clock()
print(len(a))
print("For loop list (After): {}Mb".format(memory_profiler.memory_usage()))
print("Took {} Seconds".format(t4-t3))




"""
print("List Comprehension (Before):{}Mb".format(memory_profiler.memory_usage()))

t1 = time.clock()
y = [x*x for x in range(1,10000000)]
t2 = time.clock()
print(len(y))
print("List Comprehension (After): {}Mb".format(memory_profiler.memory_usage()))
print("Took {} Seconds".format(t2-t1))
"""
