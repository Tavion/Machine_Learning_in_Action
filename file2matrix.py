import numpy as np


def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         # get the number of lines in the file
    returnMat = np.zeros((numberOfLines,3))        # prepare matrix to return
    classLabelVector = []                       # prepare labels return
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

mat, vec = file2matrix('datingTestSet.txt')

print(mat)

print(vec)
