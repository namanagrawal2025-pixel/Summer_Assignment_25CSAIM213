def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    result = "".join(compressed)
    if len(result) < len(s):
        return result
    return s

def main():
    text = "aabcccccaaa"
    result = compress_string(text)
    print(result)

main()
