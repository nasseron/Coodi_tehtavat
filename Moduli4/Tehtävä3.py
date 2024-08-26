list_num = []
while True:
    try:
        num_list = int(input("Enter a number(or type 'str' to finish): "))
        list_num.append(num_list)
    except ValueError:
        break
    if list_num:
        print(min(list_num), max(list_num))
    else:
        print("Lupettaa ohjelma")