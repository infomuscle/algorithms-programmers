import time

testList = [[1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]
testDict = [{1:9}, {2:8}, {3:7}, {4:6}, {5:5}, {6:4}, {7:3}, {8:2}, {9:1}]



start = time.time()
print(testList[0][1])
print("time = ", time.time() - start)

start = time.time()
print(testDict[0][1])
print("time = ", time.time() - start)