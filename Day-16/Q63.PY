def find_pair_with_sum(arr, target_sum):
    seen_numbers = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen_numbers:
            return complement, num
        seen_numbers.add(num)
    return None

def main():
    numbers = [10, 20, 35, 50, 75, 80]
    target = 70
    result = find_pair_with_sum(numbers, target)
    print(result)

main()
