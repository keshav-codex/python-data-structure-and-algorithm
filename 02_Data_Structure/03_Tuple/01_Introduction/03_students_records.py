'''
Student Record — Tuple Access & Unpacking

Create a tuple from taking user input containing:

Student ID   Name    Age     Course     Percentage

Display the information using tuple unpacking.

Also calculate whether the student has passed based on the percentage.
'''

print("Enter students detils")

student_id = input("Enter student Id : ")
name = input("Enter student Name : ")
age = int(input("Enter student age : "))
course = input("Enter course of students : ")
percentage = float(input("Enter percenatage : "))

student_record = (student_id,name,age,course,percentage)

student_id, name, age, course, percentage = student_record

status = 'Pass' if percentage >= 40.00 else 'Fail'

print(f"""
Student record
************
Id : {student_id}
Name : {name}
Age : {age}
Course : {course}
Percentage : {percentage}
Status : {status}
""")