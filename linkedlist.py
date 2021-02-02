# A simple Python program for traversal of a linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head

# insert first
    def insertFirst(self, num):
        node= Node(num)

        if self.head == None:
            self.head = node
            print("insert first successfully")

        else:

            node.next = self.head
            temp = self.head
            self.head = None

            self.head =  node
            print("insert first successfully")

# delete first
    def del_first(self ):
        temp = self.head
        while(temp.next.next != None):
            temp = temp.next

        temp.next = None
        print('delete last element successfully')


# get size of linked list

    def getSize(self):
        # here traversing  logic
        size_list =0
        temp = self.head
        while (temp!= None):

            temp= temp.next
            size_list =size_list+1

        print(f"size of linked list {size_list}")
        return size_list

# add element at given position
    def inserAtPos(self , pos , data):


        # get lenght of list by calling getSize function
        size_list= self.getSize()
        if (pos > size_list and pos < 0):
            print("invalid  position enter  plz try again")


        # create node
        node = Node(data)

        temp = self.head
        for n in range(size_list):
            if n == pos-1:
                node.next=temp.next
                temp.next=node
                print('insert data successfully')

            temp=temp.next



    def updateAtPos(self , pos , newData):
        # no need to create new node because here we update at given postion

        # get lenght of list by calling getSize function
        size_list= self.getSize()
        if (pos > size_list and pos < 0):
            print("invalid  position enter  plz try again")

        temp = self.head
        for n in range(size_list):
            if n == pos-1:
                temp.data= newData
                print(f"update {newData} at position {pos} sucessfully")


            temp=temp.next


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    #
    # llist.insertFirst(10)
    # llist.insertFirst(20)
    # llist.insertFirst(30)
    # llist.insertFirst(40)
    # llist.insertFirst(50)
    #
    # llist.printList()
    # print(f"--------------------------------")
    # llist.del_first()
    # llist.printList()
    # print(f"--------------------------------")
    # print(llist.getSize())
    # print(f"--------------------------------")
    # llist.inserAtPos(2,21)
    # llist.printList()
    # print(f"--------------------------------")
    #


    def menu():
        print("1 : insert element at first postion ")
        print("2 : Display list ")
        print("3 : delete element last element ")
        print("4 : insert element at given postion  ")
        print("5 : get size of list ")
        print("6 : update at postion ")
        print("0: exit")
        choice =int ( input())
        return choice

    choice =1
    while(choice !=0):
        choice= menu()

        if choice==1:
            llist.insertFirst(input("enter element : "))
        elif choice==2:
            llist.printList()
        elif choice==3:
            llist.del_first()
        elif choice==4:
            llist.inserAtPos(int(input("enter position : ")) , input("enter data : "))
        elif choice == 6:
            llist.updateAtPos(int(input("enter position : ")), input("enter new data : "))
        elif choice==5:
            print(llist.getSize())
        else:
            exit(0)










