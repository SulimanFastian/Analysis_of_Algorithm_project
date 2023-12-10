import os

class LempelZivDecompression:
    def __init__(self, filename):
        self.filename = filename
        self.window_size = 12  # Adjust the window size as needed

    def decompress(self):
        with open(self.filename, 'rb') as file:
            compressed_data = file.read()

        decompressed_data = bytearray()
        position = 0

        while position < len(compressed_data):
            token = compressed_data[position]
            position += 1

            if token == 0:
                # Literal copy
                decompressed_data.append(compressed_data[position])
                position += 1
            else:
                # Backward copy
                offset = token
                length = compressed_data[position]
                position += 1

                for _ in range(length + 1):
                    decompressed_data.append(decompressed_data[-offset])

        # Write decompressed data to text file
        output_filename = os.path.splitext(self.filename)[0] + "_decompressed_lz77.txt"
        with open(output_filename, 'wb') as output_file:
            output_file.write(decompressed_data)

# Usage
file_names = ["Zero_entropy/1000.txt", "Zero_entropy/10000.txt", "Zero_entropy/100000.txt"]
for compressed_file_name in file_names:
    lz77_decompression = LempelZivDecompression(compressed_file_name)
    lz77_decompression.decompress()
