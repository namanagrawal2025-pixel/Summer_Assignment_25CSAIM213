def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def main():
    text = "python"
    result = reverse_string(text)
    print(result)

main()
