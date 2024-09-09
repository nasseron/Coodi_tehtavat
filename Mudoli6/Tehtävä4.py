def num_list(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum
my_list = [2,4,6,8]
numbers_sum  = num_list(my_list)
print("The result of the numbers in my_lit is",numbers_sum)