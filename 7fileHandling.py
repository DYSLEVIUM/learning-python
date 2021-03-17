# 	files need to be created, openend, worked and then closed
# 	we can open a file by using the open(filename,mode+category) function

# 	different modes for opening a file, default is "r"
# => "r" -> read
# => "a" -> append
# => "w" -> write
# => "x" -> create

# 	different categories of handling file
# 	=> "t" -> text
# 	=> "b" -> binary

# 	Reading a file

f = open("inp.txt", "rt")
print(f.read(2))  # 	reading file, blank parameter means whole file
print(f.read(5))
f.close()

f = open("inp.txt", "rt")
print("Read line by line ", f.readline())  # 	line by line output
f.close()

f = open("inp.txt", "rt")
print("Read line 3 ", f.readline(3))  # 	read line 3 bytes from first line
f.close()

f = open("inp.txt", "rt")
print("Read lines separately :", f.readlines())  # 	read lines separately
f.close()

print("\n")

# 	looping over a file object
f = open("inp.txt", "rt")
for line in f:
    print(line)
f.close()

# 	writing to a file

f = open("inp2.txt", "w")
f.write("C++ is superior to python")
f.close()

f = open("inp2.txt", "a")
f.write("C++ is better than python")
f.close()

# 	creating a file
import os

if not os.path.exists("inp3.txt"):
    f = open("inp3.txt", "x")
    f.write("New file created with python")

# 	deleting a file
f = open("inp4.txt", "x")
f.write("creating file just to delete it")

if os.path.exists("inp4.txt"):
    os.remove("inp4.txt")
else:
    print("file DNE")

# 	deleting a folder

folderName = "yo"
# os.mkdir(folderName)
os.rmdir(folderName)