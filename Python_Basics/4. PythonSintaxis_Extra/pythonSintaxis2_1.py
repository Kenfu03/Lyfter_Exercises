price = int(input("Enter the price to calculate the discount: "))
final_price = 0
discount = 0

if price >= 100:
    discount = price * 0.1
else:
    discount =  price * 0.02

final_price = price - discount
print(f"The total price after discount is: {final_price}")