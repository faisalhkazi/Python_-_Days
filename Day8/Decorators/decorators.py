# def change_letter(type):
#
#
#     def uppercase(text):
#         print(text.upper())
#
#     def lowercase(text):
#         print(text.lower())
#
#     if type == "upp":
#         return uppercase
#
#     elif type == "low":
#         return lowercase
#
# operation = change_letter("upp")
#
# operation("Manchester_United")

def decorated_text(function):

    def another_function(word):

        print("Hello")
        function(word)
        print("Thank you. Bye!!! \n \n")

    return another_function

def uppercase(text):
    print(text.upper())

def lowercase(text):
    print(text.lower())

decorated_uppercase = decorated_text(uppercase)

decorated_uppercase("Manchester_United")

decorated_lowercase = decorated_text(lowercase)

decorated_lowercase("MANCHESTER_UNITED")
