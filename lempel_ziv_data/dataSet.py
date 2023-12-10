import random
import string

def generate_low_entropy_file(file_path, text_length, patterns, repetition):
    repeated_text = ''.join(pattern * repetition for pattern in patterns)
    remaining_length = text_length - len(repeated_text)
    
    if remaining_length > 0:
        random_characters = ''.join(random.choice(string.ascii_lowercase) for _ in range(remaining_length))
        text = repeated_text + random_characters
    else:
        text = repeated_text[:text_length]

    with open(file_path, 'w') as file:
        file.write(text)

# Generate a low entropy file with three different patterns repeating
low_entropy_file_path = 'low_entropy_three_patterns.txt'
generate_low_entropy_file(low_entropy_file_path, 10000, ['abcd', 'efgh', 'ijkl'], 1000)

print("Low entropy LZ77-sensitive file with three patterns generated successfully.")
