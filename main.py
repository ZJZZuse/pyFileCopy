import os
import re

import shutil

root = 'D:/abc/download/t/python files working'
out = 'out'
specialFile = 'info.txt'

def generateUnionName(name):
    return name[0:-1]



def main():
    folders = []
    folderKeyNames = set()

    def buidAllPath(*path):
        return os.path.join(root, *path)

    ##获取统一名称
    for i in os.listdir(root):
        if (i != out):
            folders.append(i)
            folderKeyNames.add(generateUnionName(i))

    ##构建目标目录s
    for certainName in folderKeyNames:
        path = root + '/' + out + "/" + certainName
        if (not os.path.exists(path)):
            os.mkdir(path)

    ##遍历复制改名
    for certainName in folderKeyNames:
        index = 1
        specialFileIndex = 1
        for folder in folders:
            if (generateUnionName(folder) == certainName):
                for file in os.listdir(buidAllPath(folder)):
                    if file == specialFile:
                        splitext = os.path.splitext(file)
                        shutil.copy(buidAllPath(folder, file),
                                    buidAllPath(out, certainName,
                                                "%s-%s-%s%s" % (
                                                certainName, splitext[0], specialFileIndex, splitext[1])))
                        specialFileIndex += 1
                        continue

                    splitext = os.path.splitext(file)
                    shutil.copy(buidAllPath(folder, file),
                                buidAllPath(out, certainName,
                                            "%s-%s%s" % (certainName, index, splitext[1])))
                    index += 1

if __name__ == '__main__':
    main()