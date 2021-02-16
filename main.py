# with open("file1.txt") as file1:
#     file1_data = file1.readlines()  # opening a file and reading it and converting it into a list
# with open("file2.txt") as file2:
#     file2_data = file2.readlines()
# # we do not have to close a file with will automatically close a file when we done with our operation
# result = [int(file_data) for file_data in file1_data if file_data in file2_data]
# print(result)

import random

"""List Comprehension is a way of creating new list from a existing list
syntax: 
new_list =[new_item for item in list]
with conditional list
new_list  = [new_item for item in list if test]
"""
fruits = ["apple", "banana", "mango"]
new_bucket = [fruit.upper() for fruit in fruits]
print(new_bucket)

student_names = ["Amit", "sundeep", "jack", "elon", "martin"]
new_list = [name for name in student_names if len(name) <=4 ]
print(new_list)


"""
 Dictionary comprehension
 syntax:
 :list can be string ,tuples, list ,or any iteratable
 new_dict = {new_key:new_value for item in list } # this will create new dictionary
Conditional Dictionary Comprehension
creating a new dictionary from a existing dictionary
syntax: 
new_dict =  {new_key:new_value for (key,value) in dictionary.items() if test}
"""
names = ["Amit", "Sundeep", "Martin", "Luci"]
student_scores = {student: random.randint(1, 100) for student in names}
print(type(student_scores))
print(student_scores)
# Now creating a dictionary from a existing dictionary
# Conditional Dictionary comprehensions
passed_student = {key: value for (key, value) in student_scores.items() if student_scores[key] > 50}
print(passed_student)
