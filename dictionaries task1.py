my_dictionary = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 88, 'Ethan': 95}
name = input('Enter the student name: ')
if name in my_dictionary:
    print(my_dictionary[name])
else:
    print('Student not found')