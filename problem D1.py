def shortest_sum(list1, list2):

    sum_list1 = sum(list1)

    sum_list2 = sum(list2)



    if sum_list1 <= sum_list2:

        return list1, sum_list1

    else:

        return list2, sum_list2



list1 = [7, 8, 3, 1, 6, 22, 10, 25, 9, 15, 1]

list2 = [2, 11, 0, 6, 3, 20, 7, 25, 6, 7]




shortest_list, shortest_sum_value = shortest_sum(list1, list2)

print("Sum of elements in list 1:", sum(list1))

print("Sum of elements in list 2:", sum(list2))

print("The list with the shortest sum is:", shortest_list)

print("Sum of the shortest list:", shortest_sum_value)




