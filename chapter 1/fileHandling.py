# File Handling
# Libraries: Built-in open()

# Concepts: Reading from and writing to files, handling file paths.

# Writing to a file
with open('/home/hariom/Desktop/example.txt', 'w') as file:
    file.write('Hello from Hari-Hacks!')

# Reading from a file
with open('/home/hariom/Desktop/example.txt', 'r') as file:
    content = file.read()
    print(content)
