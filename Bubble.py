# Python3 program to sort a doubly linked list using 
# bubble sort 
   
# structure of a node 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.prev = None
        self.next = None
   
''' Function to insert a node at the beginning of a linked list '''
def insertAtTheBegin(start_ref, data): 
    ptr1 = Node(data) 
    ptr1.data = data; 
    ptr1.next = start_ref; 
    if (start_ref != None): 
       (start_ref).prev = ptr1; 
    start_ref = ptr1; 
    return start_ref 
   
''' Function to print nodes in a given linked list '''
def printList(start): 
    temp = start; 
    print() 
    while (temp != None): 
        print(temp.data, end = ' ') 
        temp = temp.next; 
       
''' Bubble sort the given linked list '''
def bubbleSort(start): 
    swapped = 0
    lptr = None; 
    
    ''' Checking for empty list '''
    if (start == None): 
        return; 
      
    while True: 
        swapped = 0; 
        ptr1 = start;   
        while (ptr1.next != lptr):        
            if (ptr1.data > ptr1.next.data):            
                ptr1.data, ptr1.next.data = ptr1.next.data, ptr1.data 
                swapped = 1;        
            ptr1 = ptr1.next;        
        lptr = ptr1;     
        if swapped == 0: 
            break
      
# Driver code  
if __name__=='__main__': 
      
    arr = [12, 56, 2, 11, 1, 90] 
    
    ''' start with empty linked list '''
    start = None; 
    
    ''' Create linked list from the array arr[]. 
      Created linked list will be 1.11.2.56.12 '''
    for i in range(6): 
        start = insertAtTheBegin(start, arr[i]); 
    
    ''' print list before sorting '''
    print("Linked list before sorting ", end = ''); 
    printList(start); 
    
    ''' sort the linked list '''
    bubbleSort(start); 
    
    ''' print list after sorting '''
    print("\nLinked list after sorting ", end = ''); 
    printList(start); 
      
