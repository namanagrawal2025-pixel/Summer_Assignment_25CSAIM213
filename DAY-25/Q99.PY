def sort_names(names_list):
    n = len(names_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if names_list[j] > names_list[j + 1]:
                names_list[j], names_list[j + 1] = names_list[j + 1], names_list[j]
    return names_list

def main():
    names = ["Rahul", "Aman", "Vijay", "Deepak"]
    result = sort_names(names)
    print(result)

main()
