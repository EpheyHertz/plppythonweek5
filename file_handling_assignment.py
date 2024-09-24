# File Creation and Writing to File
file = open("my_file.txt", "w")  # Opens file in write mode ('w')
file.write("Hello, this is the first line.\n")
file.write("Python file handling is interesting!\n")
file.write("1234567890 - This is a line with numbers.\n")
file.close()  


file = open("my_file.txt", "r") 
content = file.read()  # Read the entire file content
print("File Content After First Write:")
print(content)
file.close()  

# File Appending
file = open("my_file.txt", "a")  # Opens file in append mode ('a')
file.write("This is the fourth line, appended.\n")
file.write("Appending more text is easy.\n")
file.write("Let's append some numbers again: 987654321.\n")
file.close()  # Close the file after appending

# Read and Display the Content Again After Appending
file = open("my_file.txt", "r")  
updated_content = file.read() 
print("\nFile Content After Appending:")
print(updated_content)
file.close() 