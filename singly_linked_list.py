class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insert_before(self.head, node)

    def set_tail(self, node):
        if self.tail is None:
            self.tail = node
            return
        self.insert_after(self.tail, node)


    def insert_before(self, node, node_to_insert):
        node_to_insert.next = node
        if node is self.head:
            self.head = node_to_insert
            return

        current_node = self.head
        while current_node != node:
            prev_node  = current_node
            current_node = current_node.next

        prev_node.next = node_to_insert

    def insert_after(self, node, node_to_insert):
        if node.next is None:
            self.tail = node_to_insert
            node.next = node_to_insert
            return
        node_to_insert.next = node.next
        node.next = node_to_insert

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        return ' -> '.join(nodes)


    def remove_node(self, node):
        if node is self.head:
            self.head = node.next
            return

        current_node = self.head
        while current_node is not node:
            prev_node = current_node
            current_node = current_node.next
        if node.next is None:
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node.next = node.next

    def remove_duplicates(self):
        node = self.head
        current_node = node
        while current_node is not None:
            next_node = node.next
            while next_node is not None and next_node.value == current_node.value:
                next_node = next_node.next
            current_node.next = next_node
            current_node = next_node



if __name__ == '__main__':
    sl_list = SinglyLinkedList()
    sl_list.set_head(Node(1))
    sl_list.set_tail(Node(1))
    sl_list.insert_after(sl_list.head, Node(1))
    sl_list.insert_after(sl_list.tail, Node(2))
    sl_list.insert_after(sl_list.tail, Node(2))
#     sl_list.insert_after(sl_list.tail, Node(2))
    # sl_list.insert_after(sl_list.tail, Node(2))
    # sl_list.insert_after(sl_list.tail, Node(3))
    # sl_list.insert_after(sl_list.tail, Node(3))
    # sl_list.insert_after(sl_list.tail, Node(3))
    # sl_list.insert_after(sl_list.tail, Node(3))
    # sl_list.insert_after(sl_list.tail, Node(6))
    # sl_list.insert_after(sl_list.tail, Node(6))
    # sl_list.insert_after(sl_list.tail, Node(6))
    # sl_list.insert_after(sl_list.tail, Node(7))
    # sl_list.insert_after(sl_list.tail, Node(7))
    print(sl_list)
    N1 = Node(24)
    sl_list.insert_after(sl_list.tail, N1)
    print(sl_list)
    N2 = Node(32)
    sl_list.insert_after(sl_list.tail, N2)
    print(sl_list)
    sl_list.remove_node(N2)
    print(sl_list)
