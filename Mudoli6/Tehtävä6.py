import math
def unit_price(diameter, price):
    radius = diameter / 100
    area = math.pi * radius ** 2
    return price / area
diameter1 = float(input("Enter the diameter of the first pizza () : "))
price1 = float(input("Enter the price of the first pizza : "))
diameter2 = float(input("Enter the diameter of the second pizza () : "))
price2 = float(input("Enter the price of the second pizza : "))
price_per_sqm1 = unit_price(diameter1, price1)
price_per_sqm2 = unit_price(diameter2, price2)
if price_per_sqm1 < price_per_sqm2:
    print("Second pizza is better value.")
else:
    print("First pizza is better value.")

