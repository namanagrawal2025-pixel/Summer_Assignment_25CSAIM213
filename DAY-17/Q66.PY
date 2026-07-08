def union_of_arrays(arr1, arr2):
    union_list = []
    for item in arr1:
        if item not in union_list:
            union_list.append(item)
    for item in arr2:
        if item not in union_list:
            union_list.append(item)
    return union_list

def main():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = union_of_arrays(list1, list2)
    print(result)

main()
