import os

file_path = "C:/Users/Kiran/PycharmProjects/pythonProject7/thinos.logs"
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File not found.")

