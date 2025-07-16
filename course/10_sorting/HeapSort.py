def Heapify(customlist, n, i):
    smallest = i
    left = (2 * i) + 1
    right = (2 * i) + 2
    if left < n and customlist[left] < customlist[smallest]:
        smallest = left
    if right < n and customlist[right] < customlist[smallest]:
        smallest = right
    if smallest != i:
        customlist[smallest], customlist[i] = customlist[i], customlist[smallest]
        Heapify(customlist, n, smallest)


def HeapSort(customlist):
    n = len(customlist)
    # Step 1: Build a Min Heap, start from the last rootnod because we are comparing the left and right child of the root node's
    for i in range(int(n / 2) - 1, -1, -1):
        Heapify(customlist, n, i)

    # Step 2: Extract elements one by one from the heap
    for j in range(n - 1, 0, -1):
        customlist[j], customlist[0] = customlist[0], customlist[j]
        Heapify(customlist, j, 0)
    return customlist


print(HeapSort([1, 8, 8, 3, 5, 6]))
