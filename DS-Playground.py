class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data, linkNode):
        linkNode = Node(data)
        if self.head is None:
            self.head = linkNode
            return
        linkVar = self.head
        while linkVar.next is not None:
            linkVar = linkVar.next
        linkVar.next = linkNode
    
    def show(self):
        if self.head is None:
            print('No linked list created or no items in the linked list \n')
            return
        else:
            linkVar = self.head
            while linkVar is not None:
                print(linkVar.data)
                linkVar = linkVar.next
    
    def intro(self):
        objLink = LinkedList()
        name_directory, size_directory = {}, {}
        no_list = int(input('How many Linked list do you want to create? '))
        
        for keys in range(1, no_list+1):
            name_directory[keys] = str(input('Name your Linked list number ' + str(keys) + ' '))
        
        for values in range(1,len(name_directory)+1):
            size_directory[name_directory[values]] = int(input('Assign a size for Linked list ' + str(name_directory[values]) + ' '))
        
        for link in size_directory:
            for size in range(1,size_directory[link]+1):
                objLink.insert(int(input('Enter integer at position ' + str(size) + ' for Linked list ' + str(link) + ' ')),link)
        objLink.show()
        
if __name__ == '__main__':
    get_Intro = LinkedList()
    get_Intro.intro()
