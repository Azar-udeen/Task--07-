#Text file with a current timestamp


import datetime

def create_text_file_with_timestamp():
    # Get the current timestamp
    current_time = datetime.datetime.now()

    # Format the timestamp as a string
    timestamp_str = current_time.strftime("%Y-%m-%d_%H-%M-%S")

    # Create a file with the timestamp as its name
    filename = f"file_{timestamp_str}.txt"

    # Create and write some content to the file
    with open(filename, 'w') as file:
        file.write("This is a text file created with a timestamp.")

    print(f"Text file '{filename}' created.")

# Call the function to create the text file
create_text_file_with_timestamp()