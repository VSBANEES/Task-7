import os

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            print(f"Content of the file '{file_name}':\n{file_content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace the file_path variable with the correct absolute path to your "guvi.txt" file
file_path = r"C:\Users\Dewan\Desktop\Thahira Java\guvi.txt"

# Example usage:
read_file(file_path)
