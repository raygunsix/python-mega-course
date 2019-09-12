from datetime import datetime

files = ["file1.txt", "file2.txt", "file3.txt"]
output_file = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"
output = ""

for file in files:
    with open(file, "r") as f:
        content = f.read()
        output += content + "\n"

with open(output_file, "w") as of:
    of.write(output)



