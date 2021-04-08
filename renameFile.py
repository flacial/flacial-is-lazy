import os
from simple_chalk import chalk

## A script for changing file names because I suck at the Terminal
def changeFileName():
    try:
        print(chalk.cyan("Example: \n\n File Path: ./myfolder/pepe/file \n Rename to: ./myfolder/pepe/file2 \n\n"))
        fileDir = input("File Path: ")
        renameTo = input("Rename to: ")
        if fileDir != renameTo:
            os.rename(fileDir, renameTo)
            return chalk.green.bold("\nFile got renamed!")
        else:
            return chalk.red("\nFile names are similar. Please use a different name")
    except FileNotFoundError:
        return chalk.red("\nFile not found!")

if __name__ == '__main__':
    print(changeFileName())