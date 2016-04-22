import numpy as np

fr = open('datingTestSet.txt')
arrayolines = fr.readlines()
numberoflines = len(arrayolines)
returnmat = np.zeros((numberoflines, 3))
classlabelvector= []
index = 0
fr.close()
for line in arrayolines:
    line = line.strip()
    listfromline = line.split('\t')
    returnmat[index, :] = listfromline[0:3]
    classlabelvector.append(listfromline[-1])
    index += 1

print(returnmat)
print(classlabelvector)


def datingClassTest()
    horatio = 0.9
    datingdatamat, datinglabels = file2matrix('datingTestSet.txt')
    normmat, ranges, minvals = autoNorm(datingdatamat)
    m = normmat.shape[0]
    numTestVecs = int(m*horatio)
    errorcount = 0.0
    for i in range(numTestVecs):
        classifierresult = classify0(normmat[i, :], normmat[numTestVecs:m,:],\datinglabels[numTestVecs:m],3)
        print("the classifier came back with: %d, the real answer is : %d"\% (classifierresult, datinglabels[i]))
        if (classifierresult != datinglabels[i]):
            errorcount += 1.0
    print"the total error rate is : %f" % (errorcount / float(numTestVecs)))
