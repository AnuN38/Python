"""1. write a prgrm to count the words "to" ,"the" present in the txt file and save the result in new file."""
ct1 = 0
ct2 = 0
f1 = "fp1.txt"
file = open(f1, "r")
data = file.read()
words = data.split()
for i in words:
    if i == "to":
        ct1 += 1
    if i == "the":
        ct2 += 1
d = {'Count of to is: ': ct1, 'Count of the is: ': ct2}
file.close()
f = open("result.txt", "w")
f.write("1. ")
f.write(str(d))
f.close()
