def intersection_of_arrays(arr1, arr2):
    intersection_list = []
    for item in arr1:
        if item in arr2 and item not in intersection_list:
            intersection_list.append(item)
    return intersection_list

def main():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection_of_arrays(list1, list2)
    print(result)

main()
