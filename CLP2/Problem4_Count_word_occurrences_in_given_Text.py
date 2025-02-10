def count_word_occurrences(text):
    words = text.lower().split()
    word_count = {}

    for word in words:
        word = word.strip(",.!?()[]{}:;\"'")
        if word:
            word_count[word] = word_count.get (word, 0) + 1

    return word_count

text = "Hello world! This is a test. Hello, this is just a test."
result = count_word_occurrences(text)
print(result)
