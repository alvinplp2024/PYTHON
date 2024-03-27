# File Creation
try:
    with open("my_file.txt", "w") as f:
        f.write("Am Alvin Learning Software Development\n")
        f.write("at plp academy\n")
        f.write("Am happy gaining my skills and taking tech world road in plp academy\n")
        print("File 'my_file.txt' created and written successfully.")
except PermissionError:
    print("Permission error occurred. Unable to create or write to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as f:
        content = f.read()
        print("Content of 'my_file.txt':")
        print(content)
except FileNotFoundError:
    print("File not found error occurred. Unable to read the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File reading process completed.\n")

# File Appending
try:
    with open("my_file.txt", "a") as f:
        f.write("This line is appended.\n")
        f.write("Appending another line here.\n")
        f.write("Appending one more line for good measure.\n")
        print("Content appended to 'my_file.txt' successfully.")
except PermissionError:
    print("Permission error occurred. Unable to append to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File appending process completed.\n")

# Error Handling
try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
        print("Content of 'nonexistent_file.txt':")
        print(content)
except FileNotFoundError:
    print("File not found error occurred. Unable to read the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Error handling process completed.")
