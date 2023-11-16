def print_unique_words(file_name):
    try:
        with open(file_name, 'r') as file:
            # Read the contents of the file
            content = file.read()

            # Split the content into words
            words = content.split()

            # Get unique words and sort them alphabetically
            unique_words = sorted(set(words))

            # Print the unique words
            print("Unique words in alphabetical order:")
            for word in unique_words:
                print(word)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


print_unique_words("c:\\chanu.txt")