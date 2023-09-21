#file handling demo
#opening a file for writing(creates the file for writing doesn't exist)
with open("demo.txt","w") as file:
        file.write("hello,world!\n")
        file.write("this is a demo file handling.\n")
#opening the same file for reading
with open ("demo.txt","r") as file:
        content = file.read()
        print("Reading the file:")
        print(content)
    #opening the file for appending
with open ("demo.txt","a")as file:
    file.write("Appending some more text.\n")
#Reading the file again after appeding
with open ("demo.txt","r")as file:
        content = file.read()
        print("\nReading the file after appending:")
        print(content)



