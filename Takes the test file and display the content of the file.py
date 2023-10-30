
#Takes the test file and display the content of the file 


def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
# Replace 'your_file.txt' with the name of the text file you want to read.
read_text_file('your_file.txt')