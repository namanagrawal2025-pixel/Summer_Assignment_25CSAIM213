def add_new_book(titles, authors):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    titles.append(title)
    authors.append(author)
    print("Book saved!")

def list_all_books(titles, authors):
    if not titles:
        print("Library is empty.")
        return
    for i in range(len(titles)):
        print("Title:", titles[i], "| Author:", authors[i])

def mini_library_system():
    titles = []
    authors = []
    while True:
        print("\n1. Add Book\n2. List Books\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_new_book(titles, authors)
        elif choice == "2":
            list_all_books(titles, authors)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def main():
    mini_library_system()

main()
