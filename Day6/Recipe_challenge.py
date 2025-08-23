import os
from pathlib import Path
from os import system

my_path = Path("D:/Learning/Day6/Recipes")

def count_recipes(path):
    counter = 0

    for txt in Path(path).glob("**/*.txt"):
        counter += 1
    return counter

#show the start menu

def start():
    system("cls")
    print("*" * 50)
    print("*" * 8 + "Welcome to the recipe administrator" + "*" * 7)
    print("*" * 50)
    print("\n")
    print(f"The recipes are in {my_path}")
    print(f"Total recipes: {count_recipes(my_path)}")

    menu_choice = 'x'
    while not menu_choice.isnumeric() or int(menu_choice) not in range(1,7):
        print("Choose an option")
        print('''
        [1] - Read recipe
        [2] - Create new recipe
        [3] - Create new category
        [4] - Eliminate recipe
        [5] - Eliminate category
        [6] - Leave the program''')
        menu_choice = input("")


def show_categories(path):
    print("Categories: ")
    categories_path = Path(path)
    categories_list = []
    counter = 1

    for folder in categories_path.iterdir():
        folder_str = str(folder.name)
        print(f"[{counter}] - {folder_str}")
        categories_list.append(folder)
        counter += 1
    return categories_list

def choose_categories(a_list):
    correct_choice = 'x'
    while not correct_choice.isnumeric() or int(correct_choice) not in range(1, len(a_list) + 1):
        correct_choice = input("\nChoose a category: ")

    return a_list[int(correct_choice) - 1 ]

def show_recipes(path):
    print("These are the recipes: ")
    recipes_path = Path(path)
    recipes_list = []
    counter = 1

    for recipe in recipes_path.glob("*.txt"):
        recipe_str = str(recipe.name)
        print(f"[{counter}] - [{recipe_str}]")
        recipes_list.append(recipe)
        counter += 1
    return recipes_list

def choose_recipes(a_list):
    recipe_choice = 'x'

    while not recipe_choice.isnumeric() or int(recipe_choice) not in range(1, len(a_list) + 1):
        recipe_choice = input('nChoose a recipe: ')

    return a_list[int(recipe_choice) - 1]

def read_recipe(recipe):
    print(Path.read_text(recipe))

def create_recipe(path):
    exists = False

    while not exists:
        print("Write a name of your recipe: ")
        recipe_name = input() + ".txt"
        print("Write your new recipe")
        recipe_content = input()
        new_path = Path(path, recipe_name)

        if not os.path.exists(new_path):
            Path.write_text(new_path, recipe_content)
            print(f"Your recipe {recipe_name} has been created")
            exists = True
        else:
            print("Sorry, that recipe already exists")


def create_category(path):
    exists = False

    while not exists:
        print("Write a name of your category: ")
        category_name = input() + ".txt"
        new_path = Path(path, category_name)

        if not os.path.exists(new_path):
            Path.mkdir(new_path)
            print(f"Your new category {category_name} has been created")
            exists = True
        else:
            print("Sorry, that category already exists")

def delete_recipe(recipe):
    Path(recipe).unlink()
    print(f"The recipe {recipe.name} has been deleted")

def delete_category(category):
    Path(category).rmdir()
    print(f"THe category {category.name} has been deleted")

def return_begining():
    return_choice = 'x'

    while return_choice.lower() != 'b':
        return_choice = input("\n Press 'b' to return to the menu: ")


finish_program = False

while not finish_program:

    menu = start()

    if menu == 1:
        my_categories = show_categories(my_path)
        my_category = choose_categories(my_categories)
        my_recipes = show_recipes(my_category)
        my_recipe = choose_recipes(my_recipes)
        read_recipe(my_recipe)
        return_begining()


    elif menu == 2:
        my_categories = show_categories(my_path)
        my_category = choose_categories(my_categories)
        create_recipe(my_category)
        return_begining()


    elif menu == 3:
        create_category(my_path)
        return_begining()


    elif menu == 4:
        my_categories = show_categories(my_path)
        my_category = choose_categories(my_categories)
        my_recipes = show_recipes(my_category)
        my_recipe = choose_recipes(my_recipes)
        delete_recipe(my_recipe)
        return_begining()


    elif menu == 5:
        my_categories = show_categories(my_path)
        my_category = choose_categories(my_categories)
        delete_category(my_category)
        return_begining()


    elif menu == 6:
        finish_program = True

