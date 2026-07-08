def convert_to_uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def main():
    text = "hello world"
    result = convert_to_uppercase(text)
    print(result)

main()
