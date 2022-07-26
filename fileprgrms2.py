"""2. write a prgrm to count the upper-case words present in the txt file and save the result in new file."""

count = 0
f2 = open("fp2.txt", "r")
data = f2.read()
for i in data:
    if i.isupper():
        count += 1
d ={'Count of upper-case words':count}
f2.close()
f = open("result.txt","a")
f.write("\n2. ")
f.write(str(d))
f.close()