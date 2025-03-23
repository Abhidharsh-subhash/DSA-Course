import numpy as np

twoDarray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(twoDarray)

print("row insertion")
newTwoDarray = np.insert(twoDarray, 0, [1, 2, 3, 4], axis=0)
print(newTwoDarray)

print("column insertion")
nTwoDarray = np.insert(twoDarray, 1, [10, 20, 30, 40], axis=1)
print(nTwoDarray)

print("insertion at the end")
row = np.array([100, 200, 300, 400]).reshape(-1, 1)
endarray = np.append(twoDarray, row, axis=1)
print(endarray)


def AccessIndexElements(array, rowIndex, colIndex):
    if rowIndex < len(array) and colIndex < len(array[0]):
        print(array[rowIndex][colIndex])
    else:
        print("Wrong Index")


AccessIndexElements(endarray, 0, 2)


def ArrayTraversal(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=" ")
        print("\n")


ArrayTraversal(twoDarray)

print("deletion")
delete = np.delete(twoDarray, 1, axis=1)
print(delete)
