#node class for singly linked lists
class Node():

    def __init__(self, data): 
        self.data = data
        self.next_node = None

#base class for member functions shared by
#LinkedList and SortedLinkedList derived classes
class LinkedListBase():

    def __init__(self):
        self.sentinel = Node('whatever')
        self.length = 0

    def get_length(self):
        return self.length

    def print_list(self):
        #print comma-delimited list
        node = self.sentinel.next_node
        while node:
            print(node.data)
            node = node.next_node

    def pop_first(self):
        #remove first node and return its data 
        retval = self.sentinel.next_node.data
        self.sentinel.next_node = self.sentinel.next_node.next_node
        self.length -= 1
        return retval

    def pop_last(self):
        #remove last node and return its data
        node = self.sentinel.next_node
        previous_node = self.sentinel
        while node.next_node:
            previous_node = node
            node = node.next_node
        previous_node.next_node = None
        self.length -= 1
        return node.data

    def pop_at(self, index):
        #remove node at index
        #and return its data
        #returns None if index oor
        if index < 0 or index >= self.length:
            return None
        node = self.sentinel
        for i in range(index):
            node = node.next_node
        #node is now the one before the one to pop
        retval = node.next_node.data
        node.next_node = node.next_node.next_node
        self.length -= 1
        return retval

    def peek_at(self, index):
        #returns data from node at index
        #if index oor, returns None
        if index < 0 or index >= self.length:
            return None
        node = self.sentinel.next_node
        for i in range(index):
            node = node.next_node
        return node.data

class LinkedList(LinkedListBase):
    #unsorted linked list

    def push_first(self, data):
        #insert new node at beginning of list
        new_node = Node(data)
        new_node.next_node = self.sentinel.next_node
        self.sentinel.next_node = new_node
        self.length += 1

    def push_last(self, data):
        #appned new node to end of list
        new_node = Node(data)
        node = self.sentinel
        while node.next_node:
            node = node.next_node
        node.next_node = new_node
        self.length += 1

    def push_at(self, index, data):
        #inserts new node in list at index.
        #returns True on success
        #return False if index oor 
        if index < 0 or index > self.get_length():
            return False
        new_node = Node(data)
        node = self.sentinel
        for i in range(index):
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
        self.length += 1
        return True

class SortedLinkedList(LinkedListBase):

    def insert(self, data):
        #insert new node after the last
        #node with smaller data
        new_node = Node(data)
        node = self.sentinel
        while node.next_node and node.next_node.data < data:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
        self.length += 1

##########TESTS#############

def test_sll():
    from random import randint
    sll = SortedLinkedList()
    for i in range(50):
        sll.insert(randint(1, 1000))
    sll.print_list()
    sll2 = SortedLinkedList()
    sll2.insert('adam')
    sll2.insert('molly.')
    sll2.insert('scott')
    sll2.insert('fred')
    sll2.print_list()

def test_ll():
    ll = LinkedList()
    ll.push_last('adam')
    ll.push_last('molly')
    ll.push_last('scott')
    ll.push_first('fred')
    ll.print_list()
    print('list length =', ll.get_length()) 
    for i in range(10):
        ll.push_at(0, '*' * i)
    for i in range(10):
        ll.push_at(ll.get_length(), '*' * i)
    ll.print_list()
    while ll.peek_at(0) != None:
        ll.pop_first()
    print("Length = ", ll.get_length())

if __name__ == "__main__":
    test_ll()
    test_sll()

