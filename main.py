num = int(input("Enter a number: "))

count = 0

# Handle the case when the number is 0
if num == 0:
    count = 1
else:
    while num != 0:
        count += 1
        num //= 10

print("Number of digits:", count)
