'''
Student Marks Management

Create a dictionary to store a student's subject-wise marks.
Take the following from the user:

Student name
Number of subjects
Subject name
Marks for each subject

Example:

Enter student name: Keshav
Enter number of subjects: 3
Subject: Python
Marks: 85
Subject: Django
Marks: 78
Subject: SQL
Marks: 90

Store the data as:
{
    "name": "Keshav",
    "marks": {
        "Python": 85,
        "Django": 78,
        "SQL": 90
    }
}

Then perform the following operations:
Display the complete student record
Display all subjects and marks
Calculate total marks
Calculate average marks
Find the subject with the highest marks
Find the subject with the lowest marks
Add a new subject and marks
Update marks of an existing subject
Delete a subject
Check whether a particular subject exists

Focus: Dictionary creation, nested dictionary, user input, key/value access,
adding, updating, deleting, traversal, and basic data processing.
'''
'''
Student Marks Management - Part 1
Take student name, subjects, and marks; store as a nested dictionary;
display the record and calculate total, average, highest and lowest marks.
'''

# ---- collect input ----

student = {}          # final record: {'name': ..., 'marks': {...}}
marks = {}             # holds subject -> mark pairs

name = input("Enter student name : ")
student['name'] = name

no_of_subjects = int(input("Enter no of subjects : "))

for i in range(no_of_subjects):
    print()
    subject = input(f"Enter name of subject {i+1} : ")
    sub_mark = int(input(f"Enter marks in {subject} : "))   # cast to int, not string
    marks[subject] = sub_mark

student['marks'] = marks


# ---- display ----

print("\nComplete record :", student)
print("Name only        :", student["name"])
print("Marks only       :", student["marks"])

print("\nSubject-wise marks :")
# unpack each (subject, mark) pair directly in the loop header --
# this is the correct way to read a dict's .items(), since each
# item is a plain tuple, not an object with named fields
for subject, sub_mark in student['marks'].items():
    print(f"(subject : {subject}  ||  mark : {sub_mark})")


# ---- totals, average, highest, lowest ----

sub_count = 0
total_marks = 0
h_marks = h_subject = None
l_marks = l_subject = None

for subject, sub_mark in student['marks'].items():
    sub_count += 1
    total_marks += sub_mark

    if h_marks is None and l_marks is None:
        # first subject seen -> use it to start both trackers
        h_marks, h_subject = sub_mark, subject
        l_marks, l_subject = sub_mark, subject
    else:
        # every later subject -> only replace if it actually beats the current record
        if sub_mark > h_marks:
            h_marks, h_subject = sub_mark, subject

        if sub_mark < l_marks:
            l_marks, l_subject = sub_mark, subject

if sub_count != 0:
    print(f"""
    Total subjects       : {sub_count}
    Total marks          : {total_marks}
    Average              : {total_marks / sub_count:.2f}
    Highest marks        : {h_marks}
    Highest marks subject: {h_subject}
    Lowest marks         : {l_marks}
    Lowest marks subject : {l_subject}
    """)