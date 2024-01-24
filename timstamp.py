import datetime

def create_file_with_timestamp():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Define the filename with the current timestamp
    filename = f"{current_timestamp}.txt"

    # Create and write content to the file
    with open(filename, 'w') as file:
        file.write(current_timestamp)

    print(f"File '{filename}' created with the content of the current timestamp.")

# Call the function to create the file
create_file_with_timestamp()
