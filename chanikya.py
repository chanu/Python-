import os
import pickle
#os.mkdir("c:\\binaryset")
os.chdir("c:\\binaryset")

file =open("c:\\binaryset\\binary.dat","ab+")

binaryset={"one","two"}

binarylist=["one","two","three","four"]

binaryData={1:"chanu",'company':"Clariont"}

# pickle.dump(binaryset,file)
# file.seek(0,0)
# output=pickle.load(file)
# print("output :",output)
# print("the cursor position is :",file.tell())


# pickle.dump(binaryData,file)
# file.seek(28,0)
# output=pickle.load(file)
# print("output :",output)
# print("the cursor position is :",file.tell())

# pickle.dump(binarylist,file)
# file.seek(75,0)
# output=pickle.load(file)
# print("output :",file.tell())
# next position is 118 :

file.seek(0,0)
output=pickle.load(file)
print("output :",output)