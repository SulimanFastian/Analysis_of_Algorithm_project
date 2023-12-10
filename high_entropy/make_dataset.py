import random
import string

# Generate a text file with high entropy (mix of alphanumeric characters)
characters = string.ascii_letters + string.digits
file_content = ''.join(random.choice(characters) for _ in range(100000))  # Adjust the length as needed

file_path = '100000.txt'
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"High entropy file '{file_path}' created.")
