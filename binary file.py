#Reading Binary File:

try:
    with open('binary_file.bin', 'rb') as file:
        data = file.read()
        # Now 'data' contains the binary data from the file.
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while reading the file.")


#Writing Binary File:

try:
    with open('binary_file.bin', 'wb') as file:
        binary_data = b'\x01\x02\x03\x04\x05'  # Replace with your binary data
        file.write(binary_data)
except IOError:
    print("An error occurred while writing the file.")