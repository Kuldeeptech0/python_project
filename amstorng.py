num = int(input("Enter a number: "))
x = num
sum = 0

while (num > 0):
    sum = sum + (num % 10) * (num % 10)* (num % 10)
    num = num // 10

if (x == sum):
    print("Armstrong number")
else:
    print("Not an Armstrong number")