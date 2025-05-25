my_dict={'Amit':45,'Sagar':56,'Sameer':87}
print(my_dict)
try:
    n=input("Enter the student's Name:")
    print(n,"'s Marks:",my_dict[n])
except:
    print("Student not found")