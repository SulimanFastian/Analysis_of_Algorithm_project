# Generate a text file with zero entropy (repeated character 'a')
file_content = 'a' * 1000  # Adjust the length as needed

file_path = '1000.txt'
with open(file_path, 'w') as file:
    file.write(file_content)

print(f"Zero entropy file '{file_path}' created.")
