def check_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    temp = s1 + s1
    if s2 in temp:
        return True
    return False

def main():
    str1 = "abcd"
    str2 = "cdab"
    result = check_rotation(str1, str2)
    print(result)

main()
