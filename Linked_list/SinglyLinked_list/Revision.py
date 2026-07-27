class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
        
class LinkedList:
        def __init__(self,head=None):
            self.head=head
            
        def insert_at_beginning(self,val):
          new=Node(val)
          if self.head!=None:
              t1=self.head
              new.next=t1
              self.head=new
          else:
              self.head=new
              
        def insert_at_postn(self,val,postn):
            temp=Node(val)
           
            if(self.head!=None):
              t1=self.head
              while(t1.next!=None):
                  if(t1.next.data==postn):
                      temp.next=t1.next
                      t1.next=temp
                      break
                  else:
                      t1=t1.next
            else:
                self.head=temp                      
          
        def insert_at_end(self,val):
            temp=Node(val)
            if(self.head!=None):
                t1=self.head  
                while(t1.next!=None):
                    t1=t1.next
                t1.next=temp
            else:
                self.head=temp
                
                
        def delete_at_position(self,val):
            if(self.head!=None):
               t1=self.head
               prev=t1
               while(t1!=None):
                   if(self.head.data==val):
                       self.head=t1.next
                       t1.next=None
                       break
                   if(t1.data==val):
                       prev.next=t1.next
                       break
                   else:
                       prev=t1
                       t1=t1.next
            else:
                print("Linked list doesnt exist")

        def print_list(self):
             t1=self.head
             while(t1.next !=None):
                  print(t1.data,end=" ")
                  t1=t1.next
             print(t1.data,end=" ")
obj=LinkedList()
obj.insert_at_beginning(3)
obj.insert_at_beginning(5)
obj.insert_at_beginning(7)
obj.insert_at_beginning(8)
obj.insert_at_postn(4,7)
obj.insert_at_end(19)
obj.delete_at_position(8)

obj.print_list()
                
                