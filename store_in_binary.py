def file_to_binary(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'rb') as input_file:
            # Read the content of the file in binary mode
            file_content = input_file.read()

            # Write the binary content to a new file
            with open(output_file_path, 'wb') as output_file:
                output_file.write(file_content)

        print(f"File '{input_file_path}' stored in binary format at '{output_file_path}'.")
    except FileNotFoundError:
        print(f"File '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file_path = "highest_entropy/100000.txt"  # Replace with the path to your file
output_file_path = "binary_output.bin"  # Replace with the desired output file path

file_to_binary(input_file_path, output_file_path)
