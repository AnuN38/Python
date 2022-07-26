name1 = input("Enter a name: ")
name2 = input("Enter another name: ")
c1 = ["T","R","U","E"]
c2 =["L","O","V","E"]
count = 0
count2 = 0
for i in name1.upper():
    if i in c1:
        count = count+1
    if i in c2:
        count2 =count2+1
for j in name2.upper():
    if j in c1:
        count = count+1
    if j in c2:
        count2 = count2 + 1

print("Your score is: ",count,count2)
