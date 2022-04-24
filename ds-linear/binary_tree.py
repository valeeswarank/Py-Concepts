class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left tree first
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        #visit base
        elements.append(self.data)

        #Vist left
        if self.left:
            elements += self.left.pre_order_traversal()

        #visit right
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []

        # Vist left
        if self.left:
            elements += self.left.pre_order_traversal()

        # visit right
        if self.right:
            elements += self.right.pre_order_traversal()

        # visit base
        elements.append(self.data)
        return elements


    def search(self, data):
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False


        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def find_minimum(self):
        if self.left is None:
            return self.data
        return self.left.find_minimum()

    def find_maximum(self):
        if self.right is None:
            return self.data
        return self.right.find_maximum()

    def calculate_sum(self):
        return sum(self.in_order_traversal())

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_minimum()
            self.data = min_val
            self.right.delete(min_val)
        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])


    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    #numbers = [15, 12, 27, 7, 14, 20, 88, 23]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    #print(numbers_tree.search(1))
    print("minimum value => ", numbers_tree.find_minimum())
    print("maximum value => ", numbers_tree.find_maximum())
    print("sum value => ", numbers_tree.calculate_sum())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    numbers_tree.delete(9)
    print(numbers_tree.in_order_traversal())
