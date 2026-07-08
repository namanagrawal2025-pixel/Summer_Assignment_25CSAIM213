def sort_words_by_length(words_list):
    n = len(words_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(words_list[j]) > len(words_list[j + 1]):
                words_list[j], words_list[j + 1] = words_list[j + 1], words_list[j]
    return words_list

def main():
    words = ["Python", "is", "a", "great", "language"]
    result = sort_words_by_length(words)
    print(result)

main()
