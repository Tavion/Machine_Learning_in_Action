import numpy as np


def file2matrix(filename):
    fr = open(filename)
    arrayolines = fr.readlines()
    numberOfLines = len(arrayolines)  # get the number of lines in the file
    returnMat = np.zeros((numberOfLines, 3))  # prepare matrix to return
    classLabelVector = []  # prepare labels return
    index = 0
    fr.close()
    for line in arrayolines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        print(type(listFromLine[-1]))

        '''if isinstance(listFromLine[-1], str):
            classLabelVector.append(listFromLine[-1])
        else:
            classLabelVector.append(int(listFromLine[-1]))'''
        index += 1
    return returnMat, classLabelVector


def autonorm(dataset):
    minvals = dataset.min(0)
    maxvals = dataset.max(0)
    ranges = maxvals - minvals
    normdataset = np.zeros(shape(dataset))
    m = dataset.shape[0]
    normdataset = dataset - tile(minvals,(m,1))
    normdataset = normdataset/tile(ranges,(m,1))
    return normdataset, ranges, minvals


def classify0(inx, dataset, labels, k):
    datasetsize = dataset.shape[0]
    diffmat = tile(inx, (datasetsize, 1)) - dataset
    sqdiffmat = diffmat**2
    sqdistances = sqdiffmat.sum(axis=1)
    distances =sqdistanves**0.5
    sorteddistindicies = distances.argsort()
    classcount = {}
    for i in range(k):
        voteilabel = labels[sorteddistindicies[i]]
        classcount[voteilabel] = classcount.get(voteilabel, 0) + 1
    sortedclasscount = sorted(classcount.iteritems(), key=operator.itemgetter(1),reverse=Ture)
    return sortedclasscount[0][0]
