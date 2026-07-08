def reverse_string():
    s = input("Enter string: ")
    print("Reversed:", s[::-1])

def check_length():
    s = input("Enter string: ")
    print("Length:", len(s))

def check_palindrome():
    s = input("Enter string: ")
    if s == s[::-1]:
        print("It is a palindrome.")
    else:
        print("Not a palindrome.")

def string_system():
    while True:
        print("\n1. Reverse String\n2. Check Length\n3. Check Palindrome\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            reverse_string()
        elif choice == "2":
            check_length()
        elif choice == "3":
            check_palindrome()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def main():
    string_system()

main()
