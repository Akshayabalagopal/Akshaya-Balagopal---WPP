'''You area student in a class of 10. your class teacher assigns you a task of entering the names of all the students in the class.
you finally want to display the names given the condition that the maximum allowed characters in a name is 15. 
as a fun task, reverse the names and display them.[Hint: slicing works when you are selecting ,aximum characters]
'''
l=[]
n=int(input("Enter no of students: "))
for i in range(n):
    name=input("Enter name: ")
    l.append(name)
print("\nReversed name: ")
for i in l:
    print(i[-1:-16:-1])