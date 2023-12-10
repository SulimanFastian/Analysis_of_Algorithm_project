import math

def shannon_entropy(text):
    # Calculate the frequency of each character in the text
    frequency = {char: text.count(char) / len(text) for char in set(text)}

    # Calculate Shannon entropy
    entropy = -sum(p * math.log2(p) for p in frequency.values() if p != 0)

    return entropy

def calculate_entropy_percentage(text):
    total_possible_symbols = len(set(text))
    entropy_percentage = (shannon_entropy(text) / math.log2(total_possible_symbols)) * 100
    return entropy_percentage

# Example usage
text1 = "aaaaaba"
text2 = "ababbb"

entropy_percentage_text1 = calculate_entropy_percentage(text1)
entropy_percentage_text2 = calculate_entropy_percentage(text2)

print(f"Shannon Entropy Percentage for '{text1}': {entropy_percentage_text1:.2f}%")
print(f"Shannon Entropy Percentage for '{text2}': {entropy_percentage_text2:.2f}%")
