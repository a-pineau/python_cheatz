class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position <= 1:
            self.setHead(nodeToInsert)
            return
        node = self.head

        count = 1
        while node is not None and count != position:
            node = node.next
            count += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                self.remove(node)
            node = node.next

    def remove(self, node):
        if node == self.head:
            self.head = node.next
            self.head.prev = None
            return
        if node is self.tail:
            self.tail = node.prev
            self.tail.next = None
            return

        print('loool')
        print(node.next.value)
        print(node.prev.value)
        node.prev.next = node.next
        node.next.prev = node.prev

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False

    def pop(self):
        value = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        return value

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        return ' <-> '.join(nodes)


if __name__ == '__main__':
    dl_list = DoublyLinkedList()
    n1 = Node(5)
    dl_list.setHead(n1)
    n2 = Node(7)
    n3 = Node(10)
    dl_list.insertAfter(dl_list.head, n2)
    print(dl_list)
    dl_list.insertAfter(dl_list.tail, n3)
    print(dl_list)
    dl_list.insertBefore(dl_list.tail, Node(25))
    print(dl_list)
    n4 = Node(-4)
    dl_list.insertBefore(dl_list.head, n4)
    print(dl_list)
    dl_list.remove(n4)
    print(dl_list)
    n5 = Node(100)
    dl_list.insertAfter(dl_list.tail, n5)
    print(dl_list)
    dl_list.remove(dl_list.tail)
    print(dl_list)
    n6 = Node(32)
    dl_list.insertAfter(dl_list.head, n6)
    print(dl_list)
    dl_list.remove(n6)
    print(dl_list)
    n7 = Node(45)
    dl_list.insertAtPosition(-1, n7)
    print(dl_list)
    dl_list.insertAtPosition(5, Node(7))
    print(dl_list)
    dl_list.removeNodesWithValue(7)
    print(dl_list)
    dl_list.removeNodesWithValue(45)
    print(dl_list)
    dl_list.removeNodesWithValue(10)
    print(dl_list)
    print(dl_list.containsNodeWithValue(5))
    print(dl_list.containsNodeWithValue(30))
    print(dl_list)
    n8, n9 = Node(8), Node(9)
    dl_list.insertAfter(dl_list.tail, n8)
    dl_list.insertAfter(dl_list.tail, n9)
    print(dl_list)
    val = dl_list.pop()
    print(dl_list)
    print(val)
    N32 = Node(32)
    dl_list.insertAfter(dl_list.tail, N32)
    print(dl_list)
    dl_list.remove(n8)
    print(dl_list)
