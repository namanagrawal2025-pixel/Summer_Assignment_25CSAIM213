def first_non_repeating(s):
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
            
    for char in s:
        if freq_dict[char] == 1:
            return char
    return None

def main():
    text = "swiss"
    result = first_non_repeating(text)
    print(result)

main()
