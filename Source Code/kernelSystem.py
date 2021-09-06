import os
architecture = "x64"

print("GalaxyOS - Version 1 - " + architecture)

def runSys():

    while True:
        command = input(">> ")

        if command == "about":
            print("GalaxyOS - Ver. 1 - " + architecture)

        elif command == "mkdir":
            folderName = input("enter the folder name: ")
            os.mkdir(folderName)
            print("folder created successfully")

        elif command == "rmdir":
            folderNameR = input("enter the folder name to remove: ")
            os.rmdir(folderNameR)
            print("folder deleted successfully") 

        elif command == "mkfl":
            fileName = input("enter the file name: ")
            fileText = input("text: ")

            # Do the command twice cuz the command is broken
            file = open(fileName + ".txt", 'w')
            file.write(fileText)
            file = open(fileName + ".txt", 'w')
            file.write(fileText)
            file.close()

            print("file created successfully")

        elif command == "open":
            openedFileName = input("enter the file name to open (with the extension): ")
            fileName2 = open(openedFileName)
            f_n = fileName2.read()
            print("output: " + f_n)

        elif command == "rmfl":
            deletedFileName = input("enter the file name to delete: ")
            os.remove(deletedFileName + ".txt")
            print("file deleted successfully") 

        elif command == "dir":
            print(os.getcwd())

        elif command == "chdir":
            directory = input("enter the folder name to change: ")
            os.walk(directory)
            os.chdir(directory)

        elif command == "cd..":
            os.chdir("..")

        else:
            print("command not valid")
