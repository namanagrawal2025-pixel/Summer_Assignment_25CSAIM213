def is_palindrome(s):
    cleaned_str = ""
    for char in s:
        if char.isalnum():
            cleaned_str += char.lower()
    
    reversed_str = ""
    for char in cleaned_str:
        reversed_str = char + reversed_str
        
    return cleaned_str == reversed_str

def main():
    text = "radar"
    result = is_palindrome(text)
    print(result)

main()
