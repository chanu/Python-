def print_unique_words(file_path):
    unique_words = set()

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                unique_words.update(words)

        sorted_unique_words = sorted(unique_words)

        for word in sorted_unique_words:
            print(word)

    except FileNotFoundError:
        print(f"File not found: {file_path}")


# Replace 'your_file.txt' with the actual path to your text file
print_unique_words('your_file.txt')
def print_unique_words(file_path):
    unique_words = set()

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                unique_words.update(words)

        sorted_unique_words = sorted(unique_words)

        for word in sorted_unique_words:
            print(word)

    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Replace 'your_file.txt' with the actual path to your text file
print_unique_words('your_file.txt')