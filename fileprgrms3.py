"""3. Write a prgrm to print odd and even position words into separate list."""

odd = []
even = []
f3 = open("fp3.txt", "r")
data = f3.read()
words = data.split()
for i in range(0, len(words)):
    if (i % 2) == 0:
        even.append(words[i])
    else:
        odd.append(words[i])
d = {"Even position words:": even, "Odd position words:": odd}
f3.close()
f = open("result.txt", "a")
f.write("3. ")
f.write(str(d))
