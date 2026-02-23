# Movie Rating System
# This program:
# 1. Removes invalid ratings (not between 1–5)
# 2. Calculates average rating
# 3. Counts number of 5-star ratings
# 4. Sorts ratings in ascending order

#List of ratings
ratings = [5, 3, 4, 6, 2, 1, 5, 0, 4, 3]

#Remove invalid ratings
valid_ratings = []

for r in ratings:
    if 1 <= r <= 5:         # valid rating condition
        valid_ratings.append(r)

print("Valid Ratings:", valid_ratings)
print("--------------------------------------")

#Calculate average rating
if len(valid_ratings) > 0:
    average = sum(valid_ratings) / len(valid_ratings)
    print("Average Rating:", average)
else:
    print("No valid ratings available")
    average = 0
print("--------------------------------------")
#Count number of 5-star ratings
five_star_count = 0

for r in valid_ratings:
    if r == 5:
        five_star_count += 1

print("Number of 5-star Ratings:", five_star_count)
print("--------------------------------------")
#Sort ratings in ascending order
valid_ratings.sort()

print("Sorted Ratings (Ascending):", valid_ratings)
print("--------------------------------------")
