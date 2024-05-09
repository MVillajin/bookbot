def main():
    find_path = "books/frankenstein.txt"
    text = get_book_text(find_path)
    num = get_num_words(text)
    print(f"{num} words!" )


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

        




main()

