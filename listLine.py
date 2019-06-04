import pathlib
import sys

# define the path
path = sys.argv[1]
currentDirectory = pathlib.Path(path)

for currentFile in currentDirectory.iterdir():  
    print(currentFile)