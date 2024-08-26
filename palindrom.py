x = int(input("Enter a number: "))
rev = 0
i=x
while (i > 0):
    rev = (rev * 10) + (i % 10)
    i = i // 10
if (x == rev):
    print("Palindrome")
else:
    print("Not Palindrome")