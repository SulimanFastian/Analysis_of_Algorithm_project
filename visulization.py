"""import pandas as pd
import matplotlib.pyplot as plt

# Load your Excel data into a Pandas DataFrame
excel_file_path = 'huffman_result.xlsx'
df = pd.read_excel(excel_file_path)

# Plot a line graph for entropy and compression achieved
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Entropy %'], marker='o', label='Entropy (%)')
plt.plot(df.index, df['Compression Achieved (%)'], marker='o', label='Compression Achieved (%)')
plt.xlabel('Text Entropy')  # Assuming the default numeric index is used
plt.ylabel('Percentage')
plt.title('Entropy and Compression Achieved for Each File')
plt.legend()
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()"""

import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a DataFrame named 'df' with the required columns
# Example data for illustration purposes
data = {'Text Entropy': ['Zero', 'Low', 'Medium', 'High', 'Highest'],
        'Entropy (%)': [0, 12, 25, 75, 83],
        'Compression Achieved (%)': [100,87, 75, 25, 16]}

df = pd.DataFrame(data)

# Plotting the line graph
plt.figure(figsize=(10, 6))
plt.plot(df['Text Entropy'], df['Entropy (%)'], marker='o', label='Entropy (%)')
plt.plot(df['Text Entropy'], df['Compression Achieved (%)'], marker='o', label='Compression Achieved (%)')
plt.xlabel('Text Entropy')
plt.ylabel('Percentage')
plt.title('Entropy and Compression Achieved for Each File')
plt.legend()
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()
