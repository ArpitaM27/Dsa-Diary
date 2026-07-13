class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None
        self.prev=None

class double_LL:
    def __init__(self):
        self.head=None
    
    def insert_mid(self,value,x):
        temp=Node(value)
        t1=self.head
        while(t1.next!=None):
            if(t1.value==x):
                break
            else:
                t1=t1.next
        t1.next.prev=temp
        temp.next=t1.next
        t1.next=temp
        temp.prev=t1
        
    def insert_end(self,value):
        temp=Node(value)
        if(self.head==None):
            self.head=temp
            return
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=temp
        temp.prev=t
    
    def insert_beg(self,val):
        temp=Node(val)
        if(self.head==None):
            self.head=temp
            return
        t1=self.head
        temp.next=self.head
        self.head=temp
        t1.prev=temp
    
    def delete(self,val):
        if(self.head==None):
            print("linked list doesnt exist")
            return
        t1=self.head
        if(t1.value==val):
            self.head=t1.next
            if(t1.next==None):
                print("Linked list is now empty")
            else:
                t1.next.prev=None
            return
        while(t1.next!=None):
            if(t1.value==val):
                t1.prev.next=t1.next
                t1.next.prev=t1.prev
                return
            else:
                t1=t1.next
        if(t1.value==val):
            t1.prev.next=None
                        
            
    def printDL(self):
        t1=self.head
        while(t1.next!=None):
           
            print(t1.value,end="<---->")
            t1=t1.next
        print(t1.value)
        
object=double_LL()
object.insert_end(5)
object.insert_end(15)
object.insert_end(25)
object.insert_beg(0)
object.insert_beg(2)
object.insert_mid(10,5)
object.insert_mid(20,15)
object.delete(2)

object.printDL()