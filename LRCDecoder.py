import os
import glob

n = 9
k = 4
r = 2
q = 8

fileList = glob.glob('Test*')
word = []
for data_file in fileList:
    f = open(data_file, "r")
    word.append(f.read(1)) #read1byte

ascii_data = [ord(ascii_info) for ascii_info in word]
print(ascii_data)
