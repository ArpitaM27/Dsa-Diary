class Node:
        def __init__(self,data,next=None):
           self.data=data
           self.next=next

class LinkedList:
    def __init__(self,head=None):
        self.head=head
        
    def insert_at_beginning(self,val):
        temp=Node(val)
        if(self.head!=None):
            t1=self.head
            temp.next=t1
            self.head=temp
        else:
            self.head=temp
    
    def insert_at_position(self,val,pos):
        temp=Node(val)
        if(self.head!=None):
            t1=self.head
            while(t1.next!=None):
                if(t1.data==pos):
                    temp.next=t1.next
                    t1.next=temp
                    break
                else:
                    t1=t1.next
        else:
            self.head=temp
    
    def delete_at_position(self,val):
        if(self.head!=None):
            t1=self.head
            prev=t1
            if (self.head.data==val):
                self.head=t1.next
                return
            while t1 is not None:
                if(t1.data==val):
                    prev.next=t1.next
                    break
                else:
                    prev=t1
                    t1=t1.next
            
    
    
    def insert_at_end(self,val):
        temp=Node(val)
        if(self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp
    
    def print_list(self):
        t1=self.head
        while(t1.next !=None):
            print(t1.data,end=" ")
            t1=t1.next
        print(t1.data,end=" ")
        
obj=LinkedList()
obj.insert_at_beginning(5)
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_position(15,10)
obj.insert_at_end(30)
obj.insert_at_end(40)
obj.delete_at_position(20)
obj.delete_at_position(5)
obj.delete_at_position(40)


obj.print_list()