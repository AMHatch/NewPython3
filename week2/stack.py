
class Stack():
    def __init__(self):
        self.data = []
        self.length = 0

    def push(self,value):
        self.data.append(value)
        self.length +=1
        
    def pop(self):
        if self.length == 0:
            return None
        removed_item = self.data.pop(value)
        self.length -= 1
        return removed_item

    def peek(self):
        if self.length = 0:
            return None
        return self.data[self.length -1]

        

