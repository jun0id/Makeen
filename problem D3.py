def sort_user_input():

    user_input = input("Enter numbers separated by spaces (add space at the end): ")
    user_input1 = input("Enter numbers separated by spaces: ")
    r= user_input+ user_input1
    numbers = [int(r) for r in r.split()]
    

    numbers.sort()
    print(numbers)

sort_user_input()
