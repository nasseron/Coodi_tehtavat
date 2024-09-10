
winter = 12, 1, 2
spring = 3, 4, 5
summar = 6,7,8
fall = 9,10,11
month_num = int(input("Enter the month number: "))
if month_num == 12 or month_num == 1 or month_num == 2 :
    print("the month number you entered is " + str(winter))
elif month_num == 3 or month_num == 4 or month_num == 5:
    print("the month number you entered is " + str(spring))
elif month_num == 6 or month_num == 7 or month_num == 8:
    print("the month number you entered is " + str(summar))
else:
    print("the month number you entered is " + str(fall))



