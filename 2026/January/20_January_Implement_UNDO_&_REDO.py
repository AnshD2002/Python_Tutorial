#POD: Implement UNDO & REDO
#Timestamp: 2026-01-20 02:00:19.399709

class Solution:

    def __init__(self):
        self.doc = ""
        self.redost = []

    # append operation
    def append(self, X):
        self.doc += X

        # clear redo stack on new write
        self.redost.clear()

    # undo operation
    def undo(self):
        if self.doc:
            last = self.doc[-1]
            self.doc = self.doc[:-1]
            self.redost.append(last)

    # redo operation
    def redo(self):
        if self.redost:
            ch = self.redost.pop()
            self.doc += ch

    # read operation
    def read(self):
        return self.doc
    
obj = Solution()
obj.append("a")
obj.append("b")
obj.append("c")
print(obj.read())  # Output: "abc"
obj.undo()
print(obj.read())  # Output: "ab"