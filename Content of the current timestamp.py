#Content of the current timestamp


import datetime

def write_timestamp_to_file(file_name):
    # Get the current timestamp
    current_time = datetime.datetime.now()

    # Format the timestamp as a string
    timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Write the timestamp to the specified file
    with open(file_name, "w") as file:
        file.write(timestamp_str)

# Specify the filename where you want to store the timestamp
file_name = "timestamp.txt"

# Call the function to write the timestamp to the file
write_timestamp_to_file(file_name)

print(f"Timestamp has been written to {file_name}")