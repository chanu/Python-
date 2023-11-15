class WordReverser:
    def reverse_words(self, input_str):
        words = input_str.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

# Example usage:
reverser = WordReverser()
result = reverser.reverse_words("Hello World")
print(result)