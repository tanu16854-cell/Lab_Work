# Sports Tournament Points Table
# This program:
# 1. Replaces negative points with 0
# 2. Finds winner and runner-up
# 3. Sorts leaderboard (descending order)

#List of team points
points = [45, 60, -10, 75, 50, -5, 65]

#Replace negative points with 0
updated_points = []

for p in points:
    if p < 0:
        updated_points.append(0)
    else:
        updated_points.append(p)

print("Updated Points:", updated_points)
print("--------------------------------------")

#Sort leaderboard in descending order
updated_points.sort(reverse=True)

print("Sorted Leaderboard:", updated_points)
print("--------------------------------------")
#Find winner and runner-up
if len(updated_points) >= 2:
    winner = updated_points[0]
    runner_up = updated_points[1]

    print("Winner Points:", winner)
    print("Runner-up Points:", runner_up)
else:
    print("Not enough teams")
print("--------------------------------------")
