def longest_word_length(words):
    max_length = 0

    for word in words:
        if len(word) > max_length:
            max_length = len(word)

    return max_length

# Test the function
word_list = ["apple", "banana", "orange", "strawberry", "kiwi"]
longest_length = longest_word_length(word_list)
print("Length of the longest word:", longest_length)
