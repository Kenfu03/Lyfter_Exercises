total_sum = 0
n = int(input("Enter the last number to add them up starting from number 1: "))

for counter in range(1, n + 1):
    total_sum += counter

print(f"The total sum is: {total_sum}")