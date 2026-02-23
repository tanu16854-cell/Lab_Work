sentence = input("Enter a sentence: ")
# t count number of alphabets
count = 0
for x in sentence:
    #to ceck x is alphabets or not
    if(x.isalpha()):
        count = count+1
        print("Number of alphabets in sentence is :",count)
