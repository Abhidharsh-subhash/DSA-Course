class Binary_Heap:
    def __init__(self, size):
        self.HeapSize = 0
        self.MaxSize = size + 1
        self.CustomList = self.HeapSize * [None]


NewBinaryHeap = Binary_Heap(10)

# Time complexity : O(1)
# Space complexity : O(N)
