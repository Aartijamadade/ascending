import os

folder_path = "C:/Users/Dipak/Desktop/abc" 
files = os.listdir(folder_path)


sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

print(sorted_files)