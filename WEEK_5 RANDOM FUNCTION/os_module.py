import os

# Current working directory
print("Current directory:", os.getcwd())

# List files and folders
print("Items:", os.listdir())

# Check path
print("students.txt exists:", os.path.exists("students.txt"))

# Check file
print("students.txt is file:", os.path.isfile("students.txt"))

# Check directory
print("data is directory:", os.path.isdir("data"))

# Join paths
path = os.path.join("data", "students.txt")
print("Combined path:", path)