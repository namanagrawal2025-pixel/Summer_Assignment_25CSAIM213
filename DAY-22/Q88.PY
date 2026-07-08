def remove_spaces(s):
    result = ""
    for char in s:
        if char != " ":
            result += char
    return result

def main():
    text = "p y t h o n"
    result = remove_spaces(text)
    print(result)

main()
