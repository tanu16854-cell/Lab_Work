# Online Exam Result Processor
# This program:
# 1. Removes lowest 2 scores
# 2. Adds grace marks of 5 to students scoring between 30–35
# 3. Counts number of students who passed (marks >= 40)

#List of student scores
scores = [25, 30, 34, 45, 50, 28, 60, 33]

# Remove lowest 2 scores
# First sort the list in ascending order
scores.sort()

# Remove first two lowest scores
scores = scores[2:]

print("Scores after removing lowest 2:", scores)
print("--------------------------------------")

#Add grace marks (5 marks for scores between 30–35)
updated_scores = []

for s in scores:
    if 30 <= s <= 35:
        s = s + 5   # add grace marks
    updated_scores.append(s)

print("Scores after grace marks:", updated_scores)
print("--------------------------------------")

#Count students who passed (marks >= 40)
pass_count = 0

for s in updated_scores:
    if s >= 40:
        pass_count += 1

print("Number of students passed:", pass_count)
print("--------------------------------------")
