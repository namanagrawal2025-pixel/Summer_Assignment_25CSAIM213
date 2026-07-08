def find_longest_word(s):
    words = s.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def main():
    text = "Python coding is magnificent"
    result = find_longest_word(text)
    print(result)

main()
