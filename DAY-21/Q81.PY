def find_string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

def main():
    text = "hello"
    result = find_string_length(text)
    print(result)

main()
