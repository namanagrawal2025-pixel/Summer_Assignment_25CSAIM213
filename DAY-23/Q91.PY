def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
        
    freq1 = {}
    freq2 = {}
    
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1
    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1
        
    return freq1 == freq2

def main():
    str1 = "listen"
    str2 = "silent"
    result = check_anagram(str1, str2)
    print(result)

main()
