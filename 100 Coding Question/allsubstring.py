# Generate all substrings

s = input("Enter string: ")

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j])
#OUTPUT
#Enter string: abhinav
#a
#ab
#abh
#abhi
#abhin
#abhina
#abhinav
#b
#bh
#bhi
#bhin
#bhina
#bhinav
#h
#hi
#hin
#hina
#hinav
#i
#in
#ina
#inav
#n
#na
#nav
#a
#av
#v
