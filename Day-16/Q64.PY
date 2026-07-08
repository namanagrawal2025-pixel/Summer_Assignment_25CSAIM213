def remove_duplicates(arr):
    unique_list = []
    for num in arr:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

def main():
    numbers = [1, 2, 2, 3, 4, 4, 4, 5]
    result = remove_duplicates(numbers)
    print(result)

main()
