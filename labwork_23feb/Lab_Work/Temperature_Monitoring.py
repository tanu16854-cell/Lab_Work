# Temperature Monitoring System
# This program:
# 1. Finds hottest and coldest day
# 2. Replaces temperatures above 45°C with "Heat Alert"
# 3. Counts number of extreme days (> 40°C)

#List of daily temperatures (in °C)
temperatures = [35, 42, 38, 46, 41, 39, 47, 33, 44, 36]

#Find hottest and coldest day
hottest = max(temperatures)
coldest = min(temperatures)

print("Hottest Temperature:", hottest)
print("Coldest Temperature:", coldest)
print("--------------------------------------")

#Replace temperatures above 45°C with "Heat Alert"
updated_temps = []

for temp in temperatures:
    if temp > 45:
        updated_temps.append("Heat Alert")
    else:
        updated_temps.append(temp)

print("Updated Temperature List:", updated_temps)
print("--------------------------------------")

#Count number of extreme days (> 40°C)
extreme_days = 0

for temp in temperatures:
    if temp > 40:
        extreme_days += 1

print("Number of Extreme Days (>40°C):", extreme_days)
print("--------------------------------------")
