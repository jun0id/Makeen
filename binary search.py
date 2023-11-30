def binary_search(key, list_):
    high = len(list_)-1
    low = 0
    while (low <= high):
        mid = int((high + low) / 2)
        if (list_ [mid] == key):
            return mid
        elif(list_[mid] < key):
            low = mid + 1
        else:
            high = mid - 1
    return -1


list_ = [10, 50, 20, 70, 80, 40, 30]
list_.sort()
key = int(input("Enter the key: "))
result= print("Index: ", binary_search(key, list_))