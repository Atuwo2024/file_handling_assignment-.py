# File Creation
try:
    # Open "my_file.txt" in write mode ('w')
    with open("my_file.txt", 'w') as file:
        # Write three lines of text to the file
        file.write("Hello, this is line 1.\n")
        file.write("12345\n")
        file.write("Python is awesome!\n")
except IOError as e:
    print("Error:", e)

# File Reading and Display
try:
    # Open "my_file.txt" in read mode ('r')
    with open("my_file.txt", 'r') as file:
        # Read and display the contents of the file
        file_contents = file.read()
        print("Contents of my_file.txt:")
        print(file_contents)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", 'a') as file:
        # Append three additional lines of text to the file
        file.write("Appending line 1.\n")
        file.write("Appending line 2.\n")
        file.write("Appending line 3.\n")
except IOError as e:
    print("Error:", e)
finally:
    print("File operations completed.")