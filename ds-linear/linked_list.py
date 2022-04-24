class Node:
    """
    Creating/Adding new node as first part and second part as next as reference to indicate the link
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    """
    To insert first, last methods object
    """
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        """
        inserting the new node at the begining of the object
        """
        node = Node(data, self.head)
        self.head = node

    def print(self):
        """
        printing the linked list objects
        """
        if self.head is None:
            print("linked list is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        """
        inserting node at the end of the object
        """
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        """
        insert values from list
        """
        self.head = None
        for d in data_list:
            self.insert_at_end(d)

    def get_length(self):
        """
        getting link list length
        """
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        """
        removing element in link list based on the index
        """
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr.next
            count +=1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count +=1


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["apple", "mango", "banana", "orange"])
    ll.print()
    print("length", ll.get_length())
    ll.remove_at(0)
    ll.insert_at(0, "jackfruit")
    ll.insert_at(3, "jackfruits")
    ll.print()