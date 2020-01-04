class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.val == None:
            return -1
        if index == 0:
            return self.val
        
        a=self.next
        i=1
        
        while a!= None:
            if i == index:
                return a.val
            a=a.next
            i+=1
        return -1
    

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.val == None:
            self.val=val
            return
        
        a=self.val
        self.val=val
        anode=self.next
        self.next=MyLinkedList()
        self.next.val=a
        self.next.next=anode
        return
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.val==None:
            self.val=val
            return
        
        s=self
        while s.next != None:
            s=s.next
        s.next = MyLinkedList()
        s.next.val = val
        return
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        i=0
        a=self
        b=a
        
        if index <= 0:
            self.addAtHead(val)
            return
        while i < index:
            i+=1
            b=a
            if a != None and a.val != None:
                a=a.next
            else:
                return
            
        b.next = MyLinkedList()
        b.next.val = val
        b.next.next = a
        return
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        i=0
        a=self
        if index < 0:
            return
        if index == 0:
            if self.val == None:
                return
            if self.next == None:
                self = None
                return
            self.val = self.next.val
            self.next = self.next.next
        
        aa = a
        while i < index:
            i += 1
            aa = a
            if aa == None:
                return
            a = a.next
        if a != None:
            aa.next = a.next
        else:
            aa.next = None
        return 
