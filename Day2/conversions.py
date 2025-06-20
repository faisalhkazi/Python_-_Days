num1 = 60
num2 = 70.5

num = num1 + num2

print(type(num1))
print(type(num2))
print(type(num))

#manual conversion

num3 = int(num2)
print(num3)
print(type(num3))

#Printing age with new age by conversion of the datatype

age = input("What is your age: ")
print(age)
print(type(age))

age = int(age)
new_age = 1 + age
print(new_age)
print(f"Your new age is: {new_age}")

print(type(age))