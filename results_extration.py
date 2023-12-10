import os
import pandas as pd
import math

class FileCompressionAnalyzer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.original_files = ["1000.txt", "10000.txt", "100000.txt"]
        self.compressed_huffman_files = ["1000_compressed.bin", "10000_compressed.bin", "100000_compressed.bin"]
        self.compressed_lz77_files = ["1000_compressed_lz77.bin", "10000_compressed_lz77.bin", "100000_compressed_lz77.bin"]

    def shannon_entropy(self, data):
        frequency = {char: data.count(char) / float(len(data)) for char in set(data)}
        entropy = -sum(p * math.log2(p) for p in frequency.values() if p != 0)
        entropy_percentage = (entropy / math.log2(256)) * 100  # Assuming 256 possible byte values
        return entropy, entropy_percentage

    def calculate_file_entropy(self, file_path):
        with open(file_path, 'r') as file:
            data = file.read()
            entropy, entropy_percentage = self.shannon_entropy(data)
        return entropy, entropy_percentage

    def analyze_compression(self):
        results = []

        for i, original_file in enumerate(self.original_files):
            original_file_path = os.path.join(self.folder_path, original_file)
            compressed_huffman_file_path = os.path.join(self.folder_path, self.compressed_huffman_files[i])
            compressed_lz77_file_path = os.path.join(self.folder_path, self.compressed_lz77_files[i])

            # Calculate entropy of the original file
            original_entropy, original_entropy_percentage = self.calculate_file_entropy(original_file_path)

            # Get size of original file in KB
            original_size_kb = os.path.getsize(original_file_path) / 1024

            # Get size of compressed files in KB
            compressed_huffman_size_kb = os.path.getsize(compressed_huffman_file_path) / 1024
            compressed_lz77_size_kb = os.path.getsize(compressed_lz77_file_path) / 1024

            # Calculate compression percentage
            compression_percentage_huffman = (1 - compressed_huffman_size_kb / original_size_kb) * 100
            compression_percentage_lz77 = (1 - compressed_lz77_size_kb / original_size_kb) * 100

            # Calculate size difference
            size_difference_huffman_kb = original_size_kb - compressed_huffman_size_kb
            size_difference_lz77_kb = original_size_kb - compressed_lz77_size_kb

            results.append({
                'File': original_file,
                'Original Size (KB)': original_size_kb,
                'Original Entropy': original_entropy,
                'Original Entropy %': original_entropy_percentage,
                'Huffman Compressed Size (KB)': compressed_huffman_size_kb,
                'Huffman Compression %': compression_percentage_huffman,
                'Huffman Size Difference (KB)': size_difference_huffman_kb,
                'LZ77 Compressed Size (KB)': compressed_lz77_size_kb,
                'LZ77 Compression %': compression_percentage_lz77,
                'LZ77 Size Difference (KB)': size_difference_lz77_kb,
            })

        # Create DataFrame and save to Excel
        df = pd.DataFrame(results)
        output_excel_path = os.path.join(self.folder_path, 'compression_results.xlsx')
        df.to_excel(output_excel_path, index=False)

        print("Analysis completed. Results saved to 'compression_results.xlsx'.")

# Usage
folder_path = "highest_entropy"  # Replace with the actual path to your folder
analyzer = FileCompressionAnalyzer(folder_path)
analyzer.analyze_compression()
