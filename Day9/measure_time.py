from datetime import *



def for_test(number):
    my_list = []
    for num in range(1, number + 1):
        my_list.append(num)
    return my_list

def while_test(number):
    my_list = []
    counter = 1
    while counter <= number:
        my_list.append(counter)
        counter += 1
    return my_list

print(for_test(15))

print(while_test(15))