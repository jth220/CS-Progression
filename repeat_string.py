theString = input("Enter character string")
num = input("Enter a positive integer")
while int(num) <= 0:
    num = input("Enter a positive integer")
    continue
else:
 multiString = theString * int(num)
print(multiString)
