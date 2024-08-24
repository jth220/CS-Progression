class Node:
    def __init__(self, value=None): #Initialises the Node, attributes such as value and a next pointer is created
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self): #O(1) Operation
        self.head = None
        self.tail = None

    def __iter__(self): #Iterates through nodes and prints node O(1)
        node = self.head
        while node:
            yield node
            node = node.next


    def insertNode(self,value,location): #O(n)
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else: 
            if location == 0: #Case for first position
              newNode.next = self.head
              self.head = newNode
            elif location == 1: #Case for last position
                newNode.next = None
                self.tail.next = newNode
            else:
                currentNode = self.head
                index = 0
                while index < location-1:
                    currentNode = currentNode.next
                    index +=1
                nextNode = currentNode.next #This process moves whatever node was after the current node to be after the newNode
                currentNode.next = newNode
                newNode.next = nextNode


    def traverse(self): #Traverses through the list and prints the value #O(n)
        if self.head is None:
            print("Single Linked List does not exist")

        else: 
            node = self.head
            while node is not None:
                print(node.value)
                node=node.next
        

    def search(self, value): #Traverses and searches through the list #O(n)
        node = self.head
        if self.head is None:
            print('No nodes present in list')
        else:
            node = self.head
            while node is not None:
                if node.value==value:
                    return f"{value} exists in list"
                node=node.next
            return f"{value} does not exist"


    def delete(self,value): #O(n)
        if self.head == None:
            print('List does not exist')

        if self.head.value == value: #If node at head needs to be deleted and case checks for if there is only 1 node
            nextNode = self.head.next
            self.head = nextNode
            if self.head is None:
                self.tail = None
            return

        
        else:
            currentNode = self.head
            while currentNode.next is not None:
             
             if currentNode.next.value == self.tail.value: #If node to be deleted is the tail
                 self.tail = currentNode
                 return

            
             if currentNode.next.value == value: #Case where node is somewhere between head and tail
                 removedNode = currentNode.next
                 nextNode = removedNode.next
                 currentNode.next = nextNode
                 return

                 



    
