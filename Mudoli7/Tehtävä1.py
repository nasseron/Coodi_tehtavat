winter = 12,1,2
spring = 3,4,5
summer = 6,7,8
fall = 9,10,11
user_input = int(input("Enter number of the month: "))
if user_input == 12 or user_input == 1 or user_input == 2:
    print("This month is in winter.")
elif user_input == 3 or user_input == 4 or user_input == 5:
    print("This month is in spring.")
elif user_input == 6 or user_input == 7 or user_input == 8:
    print("This month is in summer.")
elif user_input == 9 or user_input == 10 or user_input == 1:
    print("This month is in fall.")
