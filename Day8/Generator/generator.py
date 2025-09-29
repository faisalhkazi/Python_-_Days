# #First Example
#
# def my_function():
#     my_list = []
#     for x in range(1, 5):
#         my_list.append(x * 20)
#     return my_list
#
# def my_generator():
#     for x in range(1, 5):
#         yield x * 20
#
# print(my_function())
# print(my_generator())
#
# g = my_generator()
#
# print(next(g))
# print(next(g))
# print(next(g))
#

#Second Example
def my_generator():

    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = my_generator()

print(next(g))
print(next(g))
print(next(g))