def count_words(s):
    words = s.split()
    return len(words)

def main():
    text = "Python is fun to learn"
    result = count_words(text)
    print(result)

main()
