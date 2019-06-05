import pathlib
import sys

# define the path
path = sys.argv[1]
currentDirectory = pathlib.Path(path)

# .iterdir : list dir or file in here
for currentFile in currentDirectory.iterdir():  
    print(currentFile)
