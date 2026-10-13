words = ["apple", "banana", "watermelon", "kiwi", "orange"]

longest_word = max(words, key=lambda word: len(word))

print("Longest word:", longest_word)