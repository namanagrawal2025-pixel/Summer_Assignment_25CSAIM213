def max_occurring_char(s):
    freq_dict = {}
    for char in s:
        freq_dict[char] = freq_dict.get(char, 0) + 1
        
    max_char = s[0]
    max_count = 0
    
    for char, count in freq_dict.items():
        if count > max_count:
            max_count = count
            max_char = char
            
    return max_char

def main():
    text = "success"
    result = max_occurring_char(text)
    print(result)

main()
