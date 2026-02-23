# Attendance Tracker
# This program:
# 1. Calculates attendance percentage
# 2. Identifies students below 75% attendance
# 3. Replaces consecutive absences (0,0) with a warning flag

#Attendance list (1 = Present, 0 = Absent)
attendance = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0]

#Calculate attendance percentage
total_days = len(attendance)        # total number of days
present_days = attendance.count(1)  # count of present days

percentage = (present_days / total_days) * 100

print("Total Days:", total_days)
print("Present Days:", present_days)
print("Attendance Percentage:", percentage)
print("--------------------------------------")

#Check if attendance is below 75%
if percentage < 75:
    print("Warning: Attendance below 75%")
else:
    print("Attendance is OK")
print("--------------------------------------")
#Replace consecutive absences with warning flag
#We will create a new list to store updated attendance

updated_attendance = attendance.copy()

for i in range(len(attendance) - 1):
    if attendance[i] == 0 and attendance[i + 1] == 0:
        updated_attendance[i] = "W"       # W = Warning
        updated_attendance[i + 1] = "W"

print("Updated Attendance with Warning:", updated_attendance)
print("--------------------------------------")
