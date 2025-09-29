from collections import Counter
from collections import defaultdict



my_list = [1, 2, 3, 5, 6, 2, 6, 7, 2, 7, 8, 9, 5  ,4 ,4 ,4 ,3 , 6, 6, 7, 8, 1, 3, 4, 1, 2, 5]

my_counter = Counter(my_list)

print(my_counter)

my_dictionaries = defaultdict(lambda: "The value not found")

my_dictionaries["Name"] = "Faisal"
my_dictionaries["Age"] = 34
my_dictionaries["Height"] = "5.11 ft"

print(my_dictionaries["full name"])

print(my_dictionaries["Age"])
