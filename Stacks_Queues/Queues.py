class Queue:
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return len(self.items)==0
    
    def insert(self,val):
        self.items.append(val)
        
    def delete(self):
        if(self.isEmpty()):
            print("Queue is empty")
        else:
            return self.items.pop(0)
    
q1=Queue()
q1.insert(10)
q1.insert(20)
q1.insert(44)    
print(q1.delete())
print(q1.delete())
print(q1.delete())
print(q1.delete())
    