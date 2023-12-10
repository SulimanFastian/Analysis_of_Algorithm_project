from scipy.stats import entropy

def calculate_shannon_entropy(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            # Remove newline characters and other unwanted characters if needed
            data = ''.join(filter(lambda x: x.isprintable(), data))
            # Convert characters to ASCII values
            ascii_values = [ord(char) for char in data]
            # Calculate Shannon entropy
            entropy_value = entropy(ascii_values, base=2)
            return entropy_value
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
file_path = "high_entropy/100000.txt"  # Replace with the path to your file
shannon_entropy = calculate_shannon_entropy(file_path)

if shannon_entropy is not None:
    print(f"Shannon Entropy of the file: {shannon_entropy}")
