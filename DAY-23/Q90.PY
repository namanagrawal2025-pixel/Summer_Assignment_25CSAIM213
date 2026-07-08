def first_repeating(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

def main():
    text = "google"
    result = first_repeating(text)
    print(result)

main()
