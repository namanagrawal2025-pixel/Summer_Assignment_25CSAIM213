def find_common_chars(s1, s2):
    common = []
    freq1 = {}
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1
    for char in s2:
        if char in freq1 and freq1[char] > 0:
            common.append(char)
            freq1[char] -= 1
    return common

def main():
    str1 = "bella"
    str2 = "label"
    result = find_common_chars(str1, str2)
    print(result)

main()
