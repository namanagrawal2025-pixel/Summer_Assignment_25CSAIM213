def find_common_elements(arr1, arr2, arr3):
    common_list = []
    for item in arr1:
        if item in arr2 and item in arr3 and item not in common_list:
            common_list.append(item)
    return common_list

def main():
    list1 = [1, 5, 10, 20]
    list2 = [6, 5, 20, 80]
    list3 = [3, 5, 20, 70]
    result = find_common_elements(list1, list2, list3)
    print(result)

main()
