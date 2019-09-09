import sys, string, os
from enum import Enum
from collections import defaultdict

ddf = defaultdict(list)

def enumerateFiles(path):
    files = []
    pathToEnum = path
    items = os.listdir(pathToEnum)

    for item in items:
        if os.path.isdir(path + "\\" + item):
            files += enumerateFiles(path + "\\" + item)
        elif os.path.isfile(path + "\\" + item):
            ddf[path].append(item)
            files.append(path + "\\" + item)

    return files

if __name__ == "__main__":
    argv = sys.argv
    pathToEnumerate = argv[1]
    files = enumerateFiles(pathToEnumerate)

    print(".OPTION EXPLICIT    ; Generate errors")
    print(".Set CabinetFileCountThreshold=0;")
    print(".Set FolderFileCountThreshold=0;")
    print(".Set FolderSizeThreshold=0;")
    print(".Set MaxCabinetSize=0;")
    print(".Set MaxDiskFileCount=0;")
    print(".Set MaxDiskSize=0;")
    print(".Set CompressionType=LZX;")
    print(".Set Cabinet=on;")
    print(".Set Compress=on;")
    print("; Specify file name for new cab file;")
    print(".Set CabinetNameTemplate=kb.cab;")

    for key in ddf:
        print("")
        cmd = ".Set DestinationDir=" + key
        print(cmd)
        
        for value in ddf[key]:
            print("\"" + key + "\\" + value + "\"")
