def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    # print(frankenstein)
    words = frankenstein.split()
    # print(f"{len(words)} words in the document")
    print(frankenstein[:100])

main()
