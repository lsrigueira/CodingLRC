import os
import constant


for i in range (0,constant.N):
    try:
        f = open("TestFile.shar"+str(i))
        print("Bit"+str(i)+"------>"+f.read())
        # Do something with the file
        f.close()
    except IOError:
         print("Bit"+str(i)+"------>Missing")
         f.close()        