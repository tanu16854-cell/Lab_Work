# Student Marks Analyzer
# This program:
# 1. Removes invalid marks (less than 0 or greater than 100)
# 2. Calculates average marks
# 3. Finds topper(s)
# 4. Displays grade based on average

#Original list of marks (you can change or take input)
marks = [95, 85, 110, 76, -5, 88, 92, 67]

#Remove invalid marks
valid_marks = []   # new list to store valid marks

for m in marks:
    if 0 <= m <= 100:   # condition for valid marks
        valid_marks.append(m)

print("Valid Marks:", valid_marks)
print("--------------------------------------")
#Calculate average
if len(valid_marks) > 0:
    total = sum(valid_marks)
    average = total / len(valid_marks)
    print("Average Marks:", average)
else:
    print("No valid marks available")
    average = 0
print("--------------------------------------")
#Find topper(s)
if len(valid_marks) > 0:
    highest = max(valid_marks)   # maximum marks
    toppers = []

    for m in valid_marks:
        if m == highest:
            toppers.append(m)

    print("Topper Marks:", toppers)
else:
    print("No topper found")
print("--------------------------------------")
# Step 5: Assign grade based on average
if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)
print("--------------------------------------")

