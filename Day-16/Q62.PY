def find_max_frequency(arr):
    frequency_dict = {}
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    max_element = arr[0]
    max_count = 0
    for num, count in frequency_dict.items():
        if count > max_count:
            max_count = count
            max_element = num
            
    return max_element

def main():
    numbers = [1, 3, 2, 1, 4, 1, 3, 2, 1, 1]
    result = find_max_frequency(numbers)
    print(result)

main()
