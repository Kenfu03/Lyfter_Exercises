seconds = int(input("Enter the time in seconds to check if is more than 10min: "))
remaining_seconds = 0

if seconds < 600:
    remaining_seconds = 600 - seconds
    print(f"The time left to reach 10min is {remaining_seconds} seconds")
elif seconds > 600:
    print("The seconds are higher than 10min")
else:
    print("The time in seconds equals 10min")