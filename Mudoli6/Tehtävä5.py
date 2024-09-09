def get_even_numbers(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    return even_numbers

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 8]
    print("Original list",my_list)
    new_list = get_even_numbers(my_list)
    print("List with even numbers:",new_list)