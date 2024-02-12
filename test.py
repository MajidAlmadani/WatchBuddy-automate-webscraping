import os
import subprocess
from tvseries_download import *

directory = "D:\Anime\مترجم\Watch\English"

folder_names = sorted([name.replace("_"," ") + "\n" for name in os.listdir(directory)])

# count = 0
# for i in folder_names:
#     process = subprocess.Popen(['python', 'web_scrabing.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#     input_data = ["a\n",i,"1\n"]
#     for line in input_data:
#         process.stdin.write(line)
#     process.stdin.close()
#     output, error = process.communicate()

#     # Print the output and error (if any)
#     print("Output:\n", output)
#     print("Error:\n", error)
#     count += 1
#     if count == 10:
#         break