import heapq
import os

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        # Change the comparison to compare based on frequency
        return self.freq < other.freq

class HuffmanEncoding:
    def __init__(self, filename):
        self.filename = filename
        self.heap = []
        self.codes = {}
        self.reverse_codes = {}

    def frequency_counter(self, data):
        frequency = {}
        for char in data:
            frequency[char] = frequency.get(char, 0) + 1
        return frequency

    def build_heap(self, frequency):
        for char, freq in frequency.items():
            node = Node(char, freq)
            heapq.heappush(self.heap, (freq, node))

    def build_tree(self):
        while len(self.heap) > 1:
            freq1, node1 = heapq.heappop(self.heap)
            freq2, node2 = heapq.heappop(self.heap)

            merged_node = Node(None, freq1 + freq2)
            merged_node.left = node1
            merged_node.right = node2

            heapq.heappush(self.heap, (freq1 + freq2, merged_node))

    def build_codes_helper(self, node, current_code):
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_codes[current_code] = node.char
            return

        self.build_codes_helper(node.left, current_code + '0')
        self.build_codes_helper(node.right, current_code + '1')

    def build_codes(self):
        root = heapq.heappop(self.heap)[1]
        self.build_codes_helper(root, '')

    def compress(self):
        with open(self.filename, 'rb') as file:
            data = file.read()

        frequency = self.frequency_counter(data.decode('latin-1'))
        self.build_heap(frequency)
        self.build_tree()
        self.build_codes()

        compressed_text = ''.join(self.codes[char] for char in data.decode('latin-1'))

        # Convert binary string to a bytearray
        compressed_bytes = bytearray()
        for i in range(0, len(compressed_text), 8):
            byte = compressed_text[i:i+8]
            compressed_bytes.append(int(byte, 2))

        # Write compressed data to binary file
        output_filename = os.path.splitext(self.filename)[0] + "_compressed.bin"
        with open(output_filename, 'wb') as output_file:
            output_file.write(bytes(compressed_bytes))

# Usage
file_names = ["lempel_ziv_data/low.txt", "lempel_ziv_data/low2.txt"]

for file_name in file_names:
    huffman = HuffmanEncoding(file_name)
    huffman.compress()
