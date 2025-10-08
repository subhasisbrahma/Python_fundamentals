"""Calculates the frequency of each word in a list and identifies the most frequent word."""


# Source list of words
WORDS_LIST = [
    'It', 'was', 'Monday', 'morning', 'Swaminathan', 'was', 'reluctant', 'to', 'open', 
    'his', 'eyes', 'he', 'considered', 'Monday', 'specially', 'unpleasant', 'in', 
    'the', 'calendar', 'After', 'the', 'delicious', 'freedom', 'of', 'Saturday', 
    'and', 'Sunday', 'it', 'was', 'difficult', 'to', 'get', 'into', 'the', 'Monday', 
    'mood', 'of', 'work', 'and', 'discipline', 'He', 'shuddered', 'at', 'the', 'very', 
    'thought', 'of', 'school', 'the', 'dismal', 'yellow', 'building', 'the', 'fire', 
    'eyed', 'Vedanayagam', 'his', 'class', 'teacher', 'and', 'headmaster', 'with', 
    'his', 'thin', 'long', 'cane'
]

# Manual Word Count
unique_words = set(WORDS_LIST)
word_counts = {word: 0 for word in unique_words}

for word in WORDS_LIST:
    word_counts[word] += 1

most_frequent_word = max(word_counts, key=word_counts.get)
max_count = word_counts[most_frequent_word]

print("--- Manual Solution ---")
print(f"Total words: {len(WORDS_LIST)}")
print(f"Unique words: {len(unique_words)}")
print(f"Word counts: {word_counts}")
print(f"Most frequent word: '{most_frequent_word}' appeared {max_count} times")


