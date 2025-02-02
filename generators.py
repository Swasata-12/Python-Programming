# A generator function returns a generator object, which can be used to generate the values one-by-one as 
# you iterate over it. As you can see, the generator function my_generator() returns a generator object, 
# which can be used to generate the values in the range 0 to 4. The next() function is used to request the 
# next value from the generator, and the generator resumes its execution until it encounters another yield 
# statement or until it reaches the end of the function.


def my_generator():
    for i in range(50):
      # Complex computations
      yield i

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in  gen:
  print(j)