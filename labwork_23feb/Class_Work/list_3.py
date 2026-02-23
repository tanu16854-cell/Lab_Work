#create a list of 20 numbers
number=[]
print("Enter any 20 numbers : ")
for i in range(20):
    num = int(input(""))
    numbers.append(num)
#displaying list
print("--------------------------------------")
print()
remove_number = int(input("Enter the number you want to remove from list :   "))
print("-----------------------------------")
print("List is : ")
print(numbers)
#frequency of number
frequency = numbers.count(remove_number)
if(frequency==0):
    print(remove_number,"is not present in list")
elif(frequency==1):
    print("As it is unique so,cann't be removed from list")
else:
    #to reverse the list
    number.reverse()
    for i in range(1,frequency):
        numbers.remove(remove_number)
    # again reverse the list to get original order
    number
