# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("Hello, this is line 1.\n")
        file.write("Line 2: 12345\n")
        file.write("Line 3: Python is awesome!\n")
    print("File created successfully.")
except PermissionError:
    print("Permission denied: Unable to create file.")
except FileNotFoundError:
    print("File not found: Unable to create file.")
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    # Open "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read the contents of the file and display them on the console
        print("Contents of my_file.txt:")
        for line in file:
            print(line, end="")
    print("\nFile reading completed.")
except FileNotFoundError:
    print("File not found: Unable to read file.")
except PermissionError:
    print("Permission denied: Unable to read file.")
finally:
    print("File reading process completed.\n")

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("Line 4: Appended line 1\n")
        file.write("Line 5: Appended line 2\n")
        file.write("Line 6: Appended line 3\n")
    print("File appended successfully.")
except FileNotFoundError:
    print("File not found: Unable to append to file.")
except PermissionError:
    print("Permission denied: Unable to append to file.")
finally:
    print("File appending process completed.")
