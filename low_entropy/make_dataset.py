import random

# Generate a text file with medium entropy (mix of characters 'a', 'b', 'c')
characters = ['a', 'b']
file_content = ''.join(random.choice(characters) for _ in range(100000))  # Adjust the length as needed

file_path = '100000.txt'
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"Medium entropy file '{file_path}' created.")
