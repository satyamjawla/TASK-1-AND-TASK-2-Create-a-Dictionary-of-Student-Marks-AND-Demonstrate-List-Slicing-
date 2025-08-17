# TASK-1-AND-TASK-2-Create-a-Dictionary-of-Student-Marks-AND-Demonstrate-List-Slicing-

Task 1: Create a Dictionary of Student Marks

my_dictionary = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 88, 'Ethan': 95}
name = input('Enter the student name: ')
if name in my_dictionary:
    print(my_dictionary[name])
else:
    print('Student not found')
    

Task 2: Demonstrate List Slicing 

numbers =list(range(1,11))
first_five=numbers[:5]
reversed_five=first_five[::-1]
print('original list of numbers:', numbers)
print('first five numbers:', first_five)
print('reversed first five elements:', reversed_five)
