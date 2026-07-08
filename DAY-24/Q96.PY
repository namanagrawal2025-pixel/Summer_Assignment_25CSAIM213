def remove_duplicate_chars(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)

def main():
    text = "programming"
    result = remove_duplicate_chars(text)
    print(result)

main()
