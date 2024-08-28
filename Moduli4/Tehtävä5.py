count = 0
max_count = 5
correct_username = 'python'
correct_password = 'Rules'
while count < max_count:
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    print(count)
    count +=1
    if username == correct_username and password == correct_password:
        print("Welcome!")
    elif count > max_count or username == correct_username and password != correct_password or username != correct_username or password != correct_password:
        print ("Wrong username or password!, access is denied.")
