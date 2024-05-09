# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("42\n")
        file.write("Another line with some text and numbers: 12345\n")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File reading process completed.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is line 4 (appended)\n")
        file.write("99\n")
        file.write("Appending more text: ABCDEFG\n")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File appending process completed.")
