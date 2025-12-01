class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Delete a node by value
    def delete(self, key):
        temp = self.head

        # If head is to be deleted
        if temp and temp.data == key:
            self.head = temp.next
            return

        # Search for key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return  # Key not found

        prev.next = temp.next

    # Search for a value
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # Print the linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ----------- Example Run -----------
ll = LinkedList()

ll.insert_at_begin(10)
ll.insert_at_begin(5)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.display()          # 5 -> 10 -> 20 -> 30 -> None

ll.delete(20)
ll.display()          # 5 -> 10 -> 30 -> None

print(ll.search(10))  # True
print(ll.search(50))  # False
