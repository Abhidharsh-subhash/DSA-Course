class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        result_list = [str(self.list[i]) for i in range(len(self.list) - 1, -1, -1)]
        return ",".join(result_list)
