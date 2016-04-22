from numpy import *
"""weboriginaldata = [[0.8, 400, 0.5, 1], [12, 134000, 0.9, 3], [0, 20000, 1.1, 2], [67, 32000, 0.1, 2]]
data = np.array(weboriginaldata)
"""


def autoNorm(dataSet):
    minvals = dataSet.min(0)
    maxvals = dataSet.max(0)
    ranges = maxvals - minvals
    m = dataSet.shape[0]
    normdataset = dataSet - tile(minvals, (m, 1))
    normdataset = normdataset/(tile(ranges, (m, 1)))
    return normdataset, ranges, minvals

