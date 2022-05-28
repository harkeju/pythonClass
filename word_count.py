text_input = input("Enter the the text you'd like to count: ")

word_count = len(text_input.split())
print(f"Your text contains {word_count} words.")