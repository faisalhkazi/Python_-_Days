import os
import shutil
import send2trash


#Create a file and write something in it and also see the list of the file inside the folder
# print(os.getcwd())
#
# file = open("day_9_test.txt", "w")
# file.write("This is my first test to write something in the file which is not present currently and will be created using this function")
# file.close()
#
# print(os.listdir())
#
# shutil.move("day_9_test.txt", "D:\\Learning\\Day8")

send2trash.send2trash("D:\\Learning\\Day8\\day_9_test.txt")

path = "D:\\Learning"

for folder, sub_folder, file in os.walk(path):
    print(f"In folder: {folder}")
    print("These are the sub folders")
    for sub in sub_folder:
        print(f"\t {sub}")
    print("These are the Files")
    for fi in file:
        print(f"\t {fi}")
    print("\t")