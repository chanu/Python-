# copyfile.py

def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()

        with open(destination_file, 'w') as destination:
            destination.write(content)

        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")

    except FileNotFoundError:
        print("File not found. Please check the file names and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    source_file = input("Enter the name of the source text file: ")
    destination_file = input("Enter the name of the destination text file: ")

    copy_file_contents(source_file, destination_file)

if __name__ == "_main_":
    main()