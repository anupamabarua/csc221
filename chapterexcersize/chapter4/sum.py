"""Compute the sum of 1 + 2 + 3 + ... + n, and print the total."""
n = int(input("Enter the number to which you want to sum: "))

running_total = 0
num = 1
while num <= n:
    running_total = running_total + num
    num = num + 1

print("The total is: ", running_total)
