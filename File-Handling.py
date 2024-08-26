"""Tasks:

File Creation:
Create a Python script (file_handling_assignment.py) that does the following:
Creates a new text file named "my_file.txt" in write mode ('w').
Write at least three lines of text to the file, including a mix of strings and numbers.


File Reading and Display:
Enhance your script to read the contents of "my_file.txt" and display them on the console.


File Appending:
Modify the script to open "my_file.txt" in append mode ('a').
Append three additional lines of text to the existing content.


Error Handling:
Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError).
"""

def create_and_write_file():
    try:
        # Create a new text file in write mode
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line with a number: 42\n")
            file.write("Third line: Python file handling example.\n")
        print("File created and initial content written successfully.")
    except Exception as e:
        print(f"An error occurred while creating or writing to the file: {e}")

def read_and_display_file():
    try:
        # Open the file in read mode and display its contents
        with open("my_file.txt", "r") as file:
            content = file.read()
        print("File content:\n")
        print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

def append_to_file():
    try:
        # Open the file in append mode and add three more lines
        with open("my_file.txt", "a") as file:
            file.write("Fourth line: Appending more text.\n")
            file.write("Fifth line: More content added with a number: 99\n")
            file.write("Sixth line: End of file handling example.\n")
        print("Additional content appended to the file successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    try:
        # Create and write initial content to the file
        create_and_write_file()

        # Read and display the file content
        read_and_display_file()

        # Append additional content to the file
        append_to_file()

        # Re-read and display the updated file content
        read_and_display_file()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File handling operations are complete.")

if __name__ == "__main__":
    main()
